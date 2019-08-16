import pickle
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def get_word2vec(news_content, size=30, txt_name='news_sentences_cut.txt'):
    with open(txt_name, 'w', encoding='utf-8') as f:
        for n in news_content:
            f.write(n + '\n')
    news_word2ve= Word2Vec(LineSentence(txt_name), size=size)

if __name__ == '__main__':
    with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_content.pk', 'rb') as f:
        news_sports = pickle.load(f)
    get_word2vec(news_sports)
    print()
