from gensim.models.word2vec import Word2Vec
from function import cut, get_word_list
from collections import defaultdict

# 以用户搜索关键词为根，扩展出8个点，这8个点再各自向外扩展8个点
def get_words_connection(keywords, word2vec_filepath):
    news_word2vec = Word2Vec.load(word2vec_filepath).wv
    root = cut(keywords).split()
    unseen = []
    seen = defaultdict(set)
    # 第一轮查找
    for word in root:
        if word.isupper() and word not in news_word2vec.vocab:
            word = word.lower()
        elif word.islower() and word not in news_word2vec.vocab:
            word = word.upper()
        try:
            new_expanding = get_word_list(news_word2vec.most_similar(word, topn=5))
        except KeyError:
            print('您输入的关键词 "%s" 不存在' % word)
            return None
        seen[word].update(new_expanding)
        unseen += new_expanding
    # 第二轮
    for word in unseen:
        new_expanding = get_word_list(news_word2vec.most_similar(word, topn=5))
        seen[word].update(new_expanding)
    return (seen, root)

if __name__ == '__main__':
    word_connection, root = get_words_connection('库里詹姆斯', r'D:\Github_project\Project_one\算法模型\data\news_sports_word2vec.w2v')
    print(word_connection, root)