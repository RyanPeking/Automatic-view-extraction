import pickle
from function import cut_by_ltp, get_postags, get_netags, get_arcs, get_roles
import re

with open(r'D:\Github_project\Project_one\算法模型\data\news_sports.pk', 'rb') as f:
    news_sports = pickle.load(f)
with open(r'D:\Github_project\Project_one\算法模型\data\view_words.pk', 'rb') as f:
    view_words = pickle.load(f)

news_sports_content_sentences = [n['content'].replace('\u3000', '').split('\\n') for n in news_sports if n['content']]

for document in news_sports_content_sentences[3200:]:
    for i, sentence in enumerate(document):
        for view_word in view_words:
            if view_word in sentence:
                print(i, view_word, sentence)
                words = cut_by_ltp(sentence)
                # print(words)
                # 词性
                postags = get_postags(words)
                # print(postags)
                # 实体
                netags = get_netags(words, postags)
                # print(netags)
                # 依存句法
                arcs = get_arcs(words, postags)
                # print(arcs)
                # 语义角色标注
                roles = get_roles(words, postags, arcs)

                # 提取人物主体，谓语，及观点
                for i, arc in enumerate(arcs):
                    # 找出符合条件的主宾关系
                    if arc.relation == 'SBV' and words[arc.head - 1] == view_word:
                        # 如果主语是代词，需要从前文找出主体
                        if postags[i] == 'r':
                            sign = 0
                            for j in range(0, len(words) + 1):
                                if netags[j] != 'O':
                                    # 找出主体的定语
                                    sign = 1
                                    if arcs[j].relation == 'ATT':
                                        print(words[j] + words[arcs[j].head - 1])
                                    else:
                                        print(words[j])
                                    break
                            if sign == 0:
                                print(words[i])
                        else:
                            print(words[i])

                        # 谓语
                        print(view_word)

                        # 提取观点，先用角色标注，后考虑引号直接拿出，再没有直接将谓语后面的句子输出
                        mark = 0
                        for role in roles:
                            if role.index == arc.head - 1:
                                for arg in role.arguments:
                                    if arg.name == 'A1':
                                        # 发现这种方法不准，例如：补充道，会把道作为宾语
                                        if arg.range.end - arg.range.start < 2:
                                            # 调整谓语
                                            view_word += ''.join(words[arg.range.start: arg.range.end + 1])
                                            print(view_word)
                                        else:
                                            mark = 1
                                            print(''.join(words[arg.range.start: arg.range.end + 1]))
                                    # 调整谓语，谓语可能有状语,例：我不知道为什么喜欢
                                    if arg.name == 'ADV':
                                        view_word = ''.join(words[arg.range.start: arg.range.end + 1]) + view_word
                                        print(view_word)
                        if mark == 0:
                            # 引号里面字少的认为不是说的话，可能是特殊词
                            pattern = re.compile(r'“(.*?)”')
                            if pattern.findall(sentence) != []:
                                for s in pattern.findall(sentence):
                                    if len(s) > 4:
                                        print(s)
                            else:
                                # 判断是不是标点符号
                                if postags[arc.head] == 'wp':
                                    print(''.join(words[arc.head + 1:]))
                                else:
                                    print(''.join(words[arc.head:]))




