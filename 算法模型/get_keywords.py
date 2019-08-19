import math
import pickle
from collections import defaultdict

# 停用词
stop_words = []
for line in open(r'D:\data\停用词.txt', 'r', encoding='utf-8'):
    stop_words.append(line.replace('\n', ''))
# 建立词频表
def get_word_document_frequency(news_content):
    word_document_frequency = defaultdict(int)
    for document in news_content:
        for word in set(document.split()):
            word_document_frequency[word] += 1
    return word_document_frequency

def idf(word, content, word_frequency):
    """Gets the inversed document frequency"""
    return math.log10(len(content) / word_frequency[word])


def tf(word, document):
    """
    Gets the term frequemcy of a @word in a @document.
    """
    words = document.split()
    return sum(1 for w in words if w == word)


def get_keywords_of_a_document(document, content, word_frequency):
    words = set(document.split())
    tfidf = [
        (w, tf(w, document) * idf(w, content, word_frequency)) for w in words
    ]
    return tfidf

# 将每个document的keyword相加
def get_keywords_of_all_document(news_content):
    word_frequency = get_word_document_frequency(news_content)
    tfidf_dict = defaultdict(float)

    for document in news_content:
        tfidf = get_keywords_of_a_document(document, news_content, word_frequency)
        for word in tfidf:
            tfidf_dict[word[0]] += word[1]

    tfidf_rank = sorted(tfidf_dict.items(), key=lambda d: d[1], reverse=True)
    # print(tfidf_rank)
    # keywords = get_word_list(tfidf_rank)
    keywords = [(word, tfidf) for (word, tfidf) in tfidf_rank if (word not in stop_words and not word.isdigit())]
    print(keywords[:30])
    return keywords

if __name__ == '__main__':
    with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_content.pk', 'rb') as f:
        news_sports_content = pickle.load(f)
    news_sports_keywords = get_keywords_of_all_document(news_sports_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_keywords.pk', 'wb') as f:
        pickle.dump(news_sports_keywords, f)


    with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization_content.pk', 'rb') as f:
        news_civilization_content = pickle.load(f)
    news_civilization_keywords = get_keywords_of_all_document(news_civilization_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization_keywords.pk', 'wb') as f:
        pickle.dump(news_civilization_keywords, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_economy_content.pk', 'rb') as f:
        news_economy_content = pickle.load(f)
    news_economy_keywords = get_keywords_of_all_document(news_economy_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_economy_keywords.pk', 'wb') as f:
        pickle.dump(news_economy_keywords, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_education_content.pk', 'rb') as f:
        news_education_content = pickle.load(f)
    news_education_keywords = get_keywords_of_all_document(news_education_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_education_keywords.pk', 'wb') as f:
        pickle.dump(news_education_keywords, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_military_content.pk', 'rb') as f:
        news_military_content = pickle.load(f)
    news_military_keywords = get_keywords_of_all_document(news_military_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_military_keywords.pk', 'wb') as f:
        pickle.dump(news_military_keywords, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_other_content.pk', 'rb') as f:
        news_other_content = pickle.load(f)
    news_other_keywords = get_keywords_of_all_document(news_other_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_other_keywords.pk', 'wb') as f:
        pickle.dump(news_other_keywords, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_polity_content.pk', 'rb') as f:
        news_polity_content = pickle.load(f)
    news_polity_keywords = get_keywords_of_all_document(news_polity_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_polity_keywords.pk', 'wb') as f:
        pickle.dump(news_polity_keywords, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_society_content.pk', 'rb') as f:
        news_society_content = pickle.load(f)
    news_society_keywords = get_keywords_of_all_document(news_society_content)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_society_keywords.pk', 'wb') as f:
        pickle.dump(news_society_keywords, f)
