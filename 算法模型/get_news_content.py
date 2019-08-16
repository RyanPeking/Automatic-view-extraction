# 对新闻语料进行分词
from function import token, cut
import pickle

def get_news_content(news):
    news_content = []
    for n in news:
        if n['content']:
            news_content.append(cut(''.join(token(n['content'].replace('\\n', '')))))
        else:
            news_content.append('')
    return news_content

if __name__ == '__main__':
    with open(r'D:\Github_project\Project_one\算法模型\data\news_sports.pk', 'rb') as f:
        news_sports = pickle.load(f)
    news_sports_content = get_news_content(news_sports)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_sports_content.pk', 'wb') as f:
        pickle.dump(news_sports_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization.pk', 'rb') as f:
        news_civilization = pickle.load(f)
    news_civilization_content = get_news_content(news_civilization)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization_content.pk', 'wb') as f:
        pickle.dump(news_civilization_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_economy.pk', 'rb') as f:
        news_economy = pickle.load(f)
    news_economy_content = get_news_content(news_economy)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_economy_content.pk', 'wb') as f:
        pickle.dump(news_economy_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_education.pk', 'rb') as f:
        news_education = pickle.load(f)
    news_education_content = get_news_content(news_education)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_education_content.pk', 'wb') as f:
        pickle.dump(news_education_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_military.pk', 'rb') as f:
        news_military = pickle.load(f)
    news_military_content = get_news_content(news_military)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_military_content.pk', 'wb') as f:
        pickle.dump(news_military_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_other.pk', 'rb') as f:
        news_other = pickle.load(f)
    news_other_content = get_news_content(news_other)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_other_content.pk', 'wb') as f:
        pickle.dump(news_other_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_polity.pk', 'rb') as f:
        news_polity = pickle.load(f)
    news_polity_content = get_news_content(news_polity)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_polity_content.pk', 'wb') as f:
        pickle.dump(news_polity_content, f)

    with open(r'D:\Github_project\Project_one\算法模型\data\news_society.pk', 'rb') as f:
        news_society = pickle.load(f)
    news_society_content = get_news_content(news_society)
    with open(r'D:\Github_project\Project_one\算法模型\data\news_society_content.pk', 'wb') as f:
        pickle.dump(news_society_content, f)

