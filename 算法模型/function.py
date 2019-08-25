# 一些重复使用的函数集

def cut(string):
    import jieba
    return ' '.join(jieba.cut(string))

def token(string):
    import re
    return re.findall(r'[\w]+', string)

# print(cut(''.join(token('新华社照片，美联，2017年5月24日\\n（体育）（26）篮球——NBA东部决赛：骑士胜凯尔特人\\n5月23日，凯尔特人队球员奥里尼克（下）在比赛中突破骑士队球员勒布朗·詹姆斯的防守上篮。\\n当日，在2016-2017赛季NBA季后赛东部决赛第四场比赛中，克利夫兰骑士队主场以112比99战胜波士顿凯尔特人队，从而以总比分3比1的优势暂时领先。\\n新华社/美联'.replace('\\n', '')))))


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




