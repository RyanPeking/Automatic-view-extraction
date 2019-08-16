from gensim.models.word2vec import Word2Vec
from function import cut, get_word_list
from collections import defaultdict

# 以用户搜索关键词为根，扩展出8个点，这8个点再各自向外扩展8个点
def get_words_connection(keywords, word2vec_filepath):
    news_sports_word2vec = Word2Vec.load(word2vec_filepath).wv
    root = cut(keywords).split()
    unseen = []
    seen = defaultdict(set)
    # 第一轮查找
    for word in root:
        try:
            new_expanding = get_word_list(news_sports_word2vec.most_similar(word, topn=8))
        except KeyError:
            print('您输入的关键词 "%s" 不存在' % word)
            return None
        seen[word].update(new_expanding)
        unseen += new_expanding
    # 第二轮
    for word in unseen:
        new_expanding = get_word_list(news_sports_word2vec.most_similar(word, topn=8))
        seen[word].update(new_expanding)
    return seen

if __name__ == '__main__':
    word_connection = get_words_connection('詹姆斯 库里', r'D:\Github_project\Project_one\算法模型\data\news_sports_word2vec.w2v')
    print(word_connection)