import pickle
from function import cut_by_ltp, get_postags, get_netags, get_arcs, get_roles
import re

with open(r'D:\Github_project\Project_one\算法模型\data\news_sports.pk', 'rb') as f:
    news_sports = pickle.load(f)
with open(r'D:\Github_project\Project_one\算法模型\data\view_words.pk', 'rb') as f:
    view_words = pickle.load(f)

news_sports_content_sentences = [n['content'].replace('\u3000', '').split('\\n') for n in news_sports if n['content']]

# print(news_sports_content_sentences[:3])

for document in news_sports_content_sentences[:10]:
    for sentence in document:
        for view_word in view_words:
            if view_word in sentence:
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
                            for j in range(i, 0, -1):
                                if netags[j] != 'O':
                                    # 找出主体的定语
                                    if arcs[j].relation == 'ATT':
                                        print(words[j] + words[arcs[j].head - 1])
                                    else:
                                        print(words[j])
                                    break
                        else:
                            print(words[i])

                        # 谓语
                        print(view_word)

                        # 提取观点，如果有引号直接拿出，没有用角色标注，再没有直接将谓语后面的句子输出
                        pattern = re.compile(r'“(.*?)”')
                        if pattern.findall(sentence) != []:
                            print(pattern.findall(sentence))
                        else:
                            mark = 0
                            for role in roles[arc.head - 1]:
                                if 'A1' in role:
                                    mark = 1
                                    print(''.join(words[role[1]: role[2] + 1]))
                            if mark == 0:
                                print(''.join(words[arc[0] - 1 : ]))

                print(view_word, sentence)


