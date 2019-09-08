from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from operator import and_
from functools import reduce
import numpy as np
import jieba
import re

from scipy.spatial.distance import cosine

def distance(v1, v2): return cosine(v1, v2)

def cut(string): return ' '.join(jieba.cut(string))


def search_engine(query, news_add_opinion_filepath, news_content_filepath, X_filepath, vectorized_filepath, page_index, page_size):
    with open(X_filepath, 'rb') as f:
        X = pickle.load(f)
    with open(vectorized_filepath, 'rb') as f:
        vectorized = pickle.load(f)
    with open(news_content_filepath, 'rb') as f:
        news_content = pickle.load(f)

    words = cut(query).split()
    word_2_id = vectorized.vocabulary_
    if all([word in word_2_id for word in words]):
        candidates_ids = [word_2_id[w] for w in words]
    else:
        return ([], 0)

    # documents_ids = [
    #     id for id, content in enumerate(news_content) if all([word.upper() in content for word in words])
    # ]
    documents_ids = []
    for id, content in enumerate(news_content):
        sign = 1
        for word in words:
            if word.isalpha() and word not in content:
                word = re.findall(word, str(content), flags=re.IGNORECASE)
                if word == []:
                    sign = 0
                    break
                else:
                    word = word[0]
            if word not in content:
                sign = 0
                break
        if sign == 1:
            documents_ids.append(id)


    # we could know the documents which contain these words
    query_vec = vectorized.transform([' '.join(words)]).toarray()[0]
    sorted_documents_id = sorted(documents_ids, key=lambda i: distance(query_vec, X[i].toarray()))

    with open(news_add_opinion_filepath, 'rb') as f:
        news_add_opinion = pickle.load(f)
    start = (page_index - 1) * page_size
    end = page_index * page_size
    news_have_opinion = [news_add_opinion[id] for id in sorted_documents_id if news_add_opinion[id]['opinion'] != []]
    news_no_opinion = [news_add_opinion[id] for id in sorted_documents_id if news_add_opinion[id]['opinion'] == []]
    search_result = news_have_opinion + news_no_opinion
    length = len(search_result)
    return (search_result[start: min(end, length)], length)

if __name__ == '__main__':
    # 输入：关键字，content文件目录，news_add_opinion文件目录
    # 输出：按照tfidf及有无观点提取的新闻排名，如果没有返回None
    search_result = search_engine('文化部门 基础设施', './news_civilization_content.pk', './news_civilization_add_opinion.pk')
    print(search_result)