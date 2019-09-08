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

# 判断一个词是否是动词，是的话返回True
# 判断一个词是否是动词，是的话返回True
def is_verb(word):
    import jieba.posseg as pseg
    for word, flat in pseg.cut(word):
        if flat != 'v': return False
    return True




