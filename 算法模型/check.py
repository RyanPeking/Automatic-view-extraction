import pickle

with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_add_opinion_0_4000.pk', 'rb') as f:
    news_sports_add_opinion_0_4000 = pickle.load(f)
print(news_sports_add_opinion_0_4000)
print(len(news_sports_add_opinion_0_4000))

with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_add_opinion_4000_4500.pk', 'rb') as f:
    news_sports_add_opinion_4000_4500 = pickle.load(f)
print(news_sports_add_opinion_4000_4500)
print(len(news_sports_add_opinion_4000_4500))

with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_add_opinion_5000_5500.pk', 'rb') as f:
    news_sports_add_opinion_5000_5500 = pickle.load(f)
print(news_sports_add_opinion_5000_5500)
print(len(news_sports_add_opinion_5000_5500))