import pickle
import re
from pyltp import Segmentor, Postagger, NamedEntityRecognizer, Parser, SementicRoleLabeller


def abstract(view_word, sentence):
    # 分词
    words = segmentor.segment(sentence)
    # 词性标注
    postags = postagger.postag(words)
    # 命名实体识别
    netags = recognizer.recognize(words, postags)
    # 依存句法
    arcs = parser.parse(words, postags)

    # 提取人物主体，谓语，及观点
    for i, arc in enumerate(arcs):
        # 主语，找出符合条件的主宾关系
        if arc.relation == 'SBV' and words[arc.head - 1] == view_word:
            # 如果主语是代词，需要从前文找出主体
            if postags[i] == 'r':
                sign = 0
                # 向前找主语
                for j in range(i, 0, -1):
                    if netags[j] != 'O':
                        # 找出主体的定语
                        sign = 1
                        if arcs[j].relation == 'ATT':
                            subject = words[j] + words[arcs[j].head - 1]
                        else:
                            subject = words[j]
                        break
                if sign == 0:
                    # 向后找主语
                    for j in range(i, len(words)):
                        if netags[j] != 'O':
                            # 找出主体的定语
                            sign = 1
                            if arcs[j].relation == 'ATT':
                                subject = words[j] + words[arcs[j].head - 1]
                            else:
                                subject = words[j]
                            break
                    # 实在找不到就用代词
                    if sign == 0:
                        subject = words[i]
            else:
                subject = words[i]

            # 谓语
            predicate = view_word

            # 观点
            view = ''

            # 提取观点，先用角色标注，后考虑引号直接拿出，再没有直接将谓语后面的句子输出
            mark = 0

            # 语义角色标注
            roles = labeller.label(words, postags, arcs)

            for role in roles:
                if role.index == arc.head - 1:
                    for arg in role.arguments:
                        if arg.name == 'A1':
                            # 发现这种方法不准，例如：补充道，会把道作为宾语
                            if arg.range.end - arg.range.start < 2:
                                # 调整谓语
                                view_word += ''.join(words[arg.range.start: arg.range.end + 1])
                                predicate = view_word
                            else:
                                mark = 1
                                view = ''.join(words[arg.range.start: arg.range.end + 1])
                        # 调整谓语，谓语可能有状语,例：我不知道为什么喜欢
                        if arg.name == 'ADV':
                            predicate = ''.join(words[arg.range.start: arg.range.end + 1]) + view_word

            if mark == 0:
                # 引号里面字少的认为不是说的话，可能是特殊词
                pattern = re.compile(r'(“.*?”)')
                if pattern.findall(sentence) != []:
                    for s in pattern.findall(sentence):
                        if len(s) > 6:
                            view += s
                if view == '':
                    # 判断是不是标点符号
                    if arc.head < len(words) and postags[arc.head] == 'wp':
                        view = ''.join(words[arc.head + 1:])
                    else:
                        view = ''.join(words[arc.head:])
            if len(view) > 4:
                return (subject, predicate, view)
    return None


def add_opinion(view_words, news_list):
    for num, document in enumerate(news_list):
        news_list[num]['opinion'] = []
        if num % 100 == 0:
            print('已执行%s%%' % (num / len(news_list) * 100))
        if document['content']:
            # news_content_sentences = document['content'].replace('\u3000', '').split('\\n').split('\n')
            news_content_sentences = re.split(r'\\n|\n', document['content'].replace('\u3000', '').replace('????', '\n'))

            for sentence in news_content_sentences:
                if len(sentence) > 200:
                    sentence_cut = re.split('[ ；。]', sentence)
                    for short_sentence in sentence_cut:
                        for view_word in view_words:
                            if view_word in short_sentence:
                                result = abstract(view_word, short_sentence)
                                if result != None:
                                    news_list[num]['opinion'].append(result)
                else:
                    for view_word in view_words:
                        if view_word in sentence:
                            result = abstract(view_word, sentence)
                            if result != None:
                                news_list[num]['opinion'].append(result)
            # print(news_list[num])
    print('执行完成')

if __name__ == '__main__':
    with open(r'D:\Github_project\Project_one\算法模型\data\view_words.pk', 'rb') as f:
        view_words = pickle.load(f)


    # 加载模型
    # # 哈工大ltp分词
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('D:\data\ltp_data_v3.4.0\cws.model')  # 加载模型
    # 得到词性
    postagger = Postagger()  # 初始化实例
    postagger.load('D:\data\ltp_data_v3.4.0\pos.model')  # 加载模型
    # 得到命名实体
    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load(r'D:\data\ltp_data_v3.4.0\ner.model')  # 加载模型
    # 依存句法分析
    parser = Parser()  # 初始化实例
    parser.load(r'D:\data\ltp_data_v3.4.0\parser.model')  # 加载模型
    # 得到语义角色标注
    labeller = SementicRoleLabeller()  # 初始化实例
    labeller.load(r'D:\data\ltp_data_v3.4.0\pisrl_win.model')  # 加载模型

    # with open(r'D:\Github_project\Project_one\算法模型\data\news_sports.pk', 'rb') as f:
    #     news_sports = pickle.load(f)
    # print('正在提取news_sports...')
    # add_opinion(view_words, news_sports)
    # print(news_sports)
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_add_opinion_22350_end.pk', 'wb') as f:
    #     pickle.dump(news_sports, f)
    # print('news_sports提取完成！')


    # with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization.pk', 'rb') as f:
    #     news_civilization = pickle.load(f)
    # print('正在提取news_civilization...')
    # add_opinion(view_words, news_civilization)
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization_add_opinion.pk', 'wb') as f:
    #     pickle.dump(news_civilization, f)
    # print('news_civilization提取完成！')

    # with open(r'D:\Github_project\Project_one\算法模型\data\news_economy.pk', 'rb') as f:
    #     news_economy = pickle.load(f)
    # print('正在提取news_economy...')
    # add_opinion(view_words, news_economy)
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_economy_add_opinion.pk', 'wb') as f:
    #     pickle.dump(news_economy, f)
    # print('news_economy提取完成！')
    #
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_education.pk', 'rb') as f:
    #     news_education = pickle.load(f)
    # print('正在提取news_education...')
    # add_opinion(view_words, news_education)
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_education_add_opinion.pk', 'wb') as f:
    #     pickle.dump(news_education, f)
    # print('news_education提取完成！')
    #
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_military.pk', 'rb') as f:
    #     news_military = pickle.load(f)
    # print('正在提取news_military...')
    # add_opinion(view_words, news_military)
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_military_add_opinion.pk', 'wb') as f:
    #     pickle.dump(news_military, f)
    # print('news_military提取完成！')
    #
    #
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_other.pk', 'rb') as f:
    #     news_other = pickle.load(f)
    # print('正在提取news_other...')
    # add_opinion(view_words, news_other)
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_other_add_opinion.pk', 'wb') as f:
    #     pickle.dump(news_other, f)
    # print('news_other提取完成！')

    with open(r'D:\Github_project\Project_one\算法模型\data\news_polity.pk', 'rb') as f:
        news_polity = pickle.load(f)
    print('正在提取news_polity...')
    add_opinion(view_words, news_polity)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_polity_add_opinion.pk', 'wb') as f:
        pickle.dump(news_polity, f)
    print('news_polity提取完成！')

    # with open(r'D:\Github_project\Project_one\算法模型\data\news_society.pk', 'rb') as f:
    #     news_society = pickle.load(f)
    # print('正在提取news_society...')
    # add_opinion(view_words, news_society[15500:])
    # with open(r'D:\Github_project\Project_one\算法模型\data\news_society_add_opinion.pk', 'wb') as f:
    #     pickle.dump(news_society, f)
    # print('news_society提取完成！')

# 释放模型
    segmentor.release()
    postagger.release()
    recognizer.release()
    parser.release()
    labeller.release()




