'''
输入：initial_word='说 表示 认为', maxsize=400
输出：maxsize个观点词
'''
import pickle
from collections import defaultdict
import synonyms
from function import get_word_list

def get_view_words(initial_word='说 表示 认为 提出', maxsize=400):
    def get_related_words_by_synonyms(initial_word, maxsize):
        unseen = initial_word.split()
        seen = defaultdict(int)
        max_size = maxsize
        # 建邻表
        adj = defaultdict(list)
        print("正在获取view_words.........")
        while unseen and len(seen) < max_size:
            if len(seen) % 100 == 0:
                print('seen length:{}'.format(len(seen)))
            node = unseen.pop(0)
            if node in seen:
                new_expanding = adj[node]
            else:
                new_expanding = [w for w in synonyms.nearby(node)[0]]
            adj[node] = new_expanding
            unseen += new_expanding
            seen[node] += 1
        print("成功获取view_words！")
        return seen

    view_words = get_related_words_by_synonyms(initial_word, maxsize)
    view_words = get_word_list(sorted(view_words.items(), key=lambda x: x[1], reverse=True))

    return view_words

if __name__ == '__main__':
    view_words = get_view_words()
    with open(r'D:\Github_project\Project_one\算法模型\data\view_words_unsift.pk', 'wb') as f:
        pickle.dump(view_words, f)