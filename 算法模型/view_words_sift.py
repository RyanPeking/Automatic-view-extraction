# 筛选view_words

import pickle
from function import is_verb

with open(r'D:\Github_project\Project_one\算法模型\data\view_words_unsift.pk', 'rb') as f:
    view_words_unsift = pickle.load(f)

print(view_words_unsift)
view_words = [view_word for view_word in view_words_unsift if is_verb(view_word)]
print(view_words)
print(len(view_words))

with open(r'D:\Github_project\Project_one\算法模型\data\view_words.pk', 'wb') as f:
    pickle.dump(view_words, f)


