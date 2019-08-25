import pickle
import pandas as pd

def drop_duplicates(news_add_opinion_filepath, news_add_opinion_drop_duplicates_filepath):
    with open(news_add_opinion_filepath, 'rb') as f:
        news_add_opinion = pickle.load(f)
    data = pd.DataFrame(news_add_opinion)
    data = data.dropna()
    data = data.drop_duplicates(subset=['content'])
    print(str(len(news_add_opinion)) + '->' + str(len(data)))
    ele_dict = {}
    data_list = []
    for i in zip(data['author'], data['content'], data['feature'], data['id'], data['opinion'], data['source'],
                 data['title'], data['url']):
        ele_dict['author'] = i[0]
        ele_dict['content'] = i[1]
        ele_dict['feature'] = i[2]
        ele_dict['id'] = i[3]
        ele_dict['opinion'] = i[4]
        opinion = []
        for o in ele_dict['opinion']:
            if len(o[2]) > 5:
                opinion.append(o)
        ele_dict['opinion'] = opinion
        ele_dict['source'] = i[5]
        ele_dict['title'] = i[6]
        ele_dict['url'] = i[7]
        data_list.append(ele_dict.copy())

    with open(news_add_opinion_drop_duplicates_filepath, 'wb') as f:
        pickle.dump(data_list, f)

if __name__ == '__main__':
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_civilization_add_opinion.pk', r'D:\Github_project\Project_one\算法模型\data\news_civilization_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_economy_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_economy_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_education_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_education_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_military_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_military_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_other_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_other_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_polity_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_polity_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_society_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_society_add_opinion_drop_duplicates.pk')
    drop_duplicates(r'D:\Github_project\Project_one\算法模型\data\news_sports_add_opinion.pk',
                    r'D:\Github_project\Project_one\算法模型\data\news_sports_add_opinion_drop_duplicates.pk')