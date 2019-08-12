# 一些重复使用的函数集

def cut(string):
    import jieba
    return ' '.join(jieba.cut(string))

def token(string):
    import re
    return re.findall(r'[\w]+', string)

# 从嵌套结构中提取第一个元素列表
def get_word_list(list):
    return [word[0] for word in list]

# 列表中若有元素在object内，返回true，否则返回false
def any_in(list, object):
    for i in list:
        if i in object:
            return True
    return False

# 哈工大ltp分词
def cut_by_ltp(sentence):
    from pyltp import Segmentor
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('D:\data\ltp_data_v3.4.0\cws.model')  # 加载模型
     # 分词
    words = segmentor.segment(sentence)
    segmentor.release()
    return words

# 得到词性
def get_postags(words):
    from pyltp import Postagger
    postagger = Postagger() # 初始化实例
    postagger.load('D:\data\ltp_data_v3.4.0\pos.model')  # 加载模型
     # 词性标注
    postags = postagger.postag(words)
    postagger.release()  # 释放模型
    return postags

# 得到命名实体
def get_netags(words, postags):
    from pyltp import NamedEntityRecognizer
    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load(r'D:\data\ltp_data_v3.4.0\ner.model')  # 加载模型
    # 命名实体识别
    netags = recognizer.recognize(words, postags)
    recognizer.release()  # 释放模型
    return netags

# 依存句法分析
def get_arcs(words, postags):
    from pyltp import Parser
    parser = Parser() # 初始化实例
    parser.load(r'D:\data\ltp_data_v3.4.0\parser.model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    # 利用依存句法提取句子主体
    parser.release()  # 释放模型
    return arcs

# 得到语义角色标注
def get_roles(words, postags, arcs):
    from pyltp import SementicRoleLabeller
    labeller = SementicRoleLabeller() # 初始化实例
    labeller.load(r'D:\data\ltp_data_v3.4.0\pisrl_win.model')  # 加载模型
    roles = labeller.label(words, postags, arcs)  # 语义角色标注
    labeller.release()  # 释放模型
    return roles

# 判断一个词是否是动词，是的话返回True
# 判断一个词是否是动词，是的话返回True
def is_verb(word):
    import jieba.posseg as pseg
    for word, flat in pseg.cut(word):
        if flat != 'v': return False
    return True


