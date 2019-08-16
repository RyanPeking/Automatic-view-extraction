# 从数据库获取新闻并分类
import pymysql
import pickle
import re
from function import any_in

conn = pymysql.connect(host='rm-8vbwj6507z6465505ro.mysql.zhangbei.rds.aliyuncs.com', port=3306, user='root', passwd='AI@2019@ai', db='stu_db')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
cur.execute('select * from news_chinese')
news = cur.fetchall()

with open(r'D:\Github_project\Project_one\算法模型\data\news.pk', 'wb') as f:
    pickle.dump(news, f)

# 分类
pattern = re.compile(r'"type":"(\w+)"')
news_sports = []# 体育
news_economy = []# 经济
news_society = []# 社会
news_polity = []# 政治法律
news_civilization = []# 文化娱乐
news_military = []# 军事
news_education = []# 教育
news_other = []# 其他

for news in news:
    news_type = pattern.findall(news['feature'])
    # 有些数据type有问题
    if news_type:
        news_type = news_type[0]
        if any_in(['球', '体育', '跳水', '自行车', '游泳', '滑冰', '马拉松', '健身', '体操'], news_type):
            news_sports.append(news)
        if any_in(['经济', '股票', '市场', '商业', '财经', '房地产', '债市', '新三板', '公司', '旅游业'], news_type):
            news_economy.append(news)
        if any_in(['社会', '环保', '图文', '生活', '事件', '组织', '动物', '医药', '卫生', '新闻', '天气', '图文', '就业', '群众', '活动', '资讯', '价值观', '谷物'], news_type):
            news_society.append(news)
        if any_in(['政治', '法律', '时事', '领导', '台湾', '国家'], news_type):
            news_polity.append(news)
        if any_in(['文化', '娱', '风土', '人情', '音乐', '宗教', '信仰', '名胜'], news_type):
            news_civilization.append(news)
        if any_in(['军事', '指挥', '军情', '武器', '装备'], news_type):
            news_military.append(news)
        if any_in(['教育'], news_type):
            news_education.append(news)
        if any_in(['其它'], news_type):
            news_other.append(news)

with open(r'D:\Github_project\Project_one\算法模型\data\news_sports.pk', 'wb') as f:
    pickle.dump(news_sports, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_economy.pk', 'wb') as f:
    pickle.dump(news_economy, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_society.pk', 'wb') as f:
    pickle.dump(news_society, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_polity.pk', 'wb') as f:
    pickle.dump(news_polity, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_civilization.pk', 'wb') as f:
    pickle.dump(news_civilization, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_military.pk', 'wb') as f:
    pickle.dump(news_military, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_education.pk', 'wb') as f:
    pickle.dump(news_education, f)
with open(r'D:\Github_project\Project_one\算法模型\data\news_other.pk', 'wb') as f:
    pickle.dump(news_other, f)

print('执行完成！')