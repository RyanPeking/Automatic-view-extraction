from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def get_X(content_filepath, X_filepath, word_2_id_filepath, vectorized_filepath):
    with open(content_filepath, 'rb') as f:
        news_content = pickle.load(f)
    vectorized = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    X = vectorized.fit_transform(news_content)
    word_2_id = vectorized.vocabulary
    with open(X_filepath, 'wb') as f:
        pickle.dump(X, f)
    with open(word_2_id_filepath, 'wb') as f:
        pickle.dump(word_2_id, f)
    with open(vectorized_filepath, 'wb') as f:
        pickle.dump(vectorized, f)

if __name__ == '__main__':
    get_X(r'D:\Github_project\data\searchengineer\news_civilization_content.pk', r'D:\Github_project\data\searchengineer\news_civilization_X.pk', r'D:\Github_project\data\searchengineer\news_civilization_word_2_id.pk', r'D:\Github_project\data\searchengineer\news_civilization_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_economy_content.pk',
          r'D:\Github_project\data\searchengineer\news_economy_X.pk',
          r'D:\Github_project\data\searchengineer\news_economy_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_economy_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_education_content.pk',
          r'D:\Github_project\data\searchengineer\news_education_X.pk',
          r'D:\Github_project\data\searchengineer\news_education_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_education_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_military_content.pk',
          r'D:\Github_project\data\searchengineer\news_military_X.pk',
          r'D:\Github_project\data\searchengineer\news_military_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_military_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_other_content.pk',
          r'D:\Github_project\data\searchengineer\news_other_X.pk',
          r'D:\Github_project\data\searchengineer\news_other_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_other_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_polity_content.pk',
          r'D:\Github_project\data\searchengineer\news_polity_X.pk',
          r'D:\Github_project\data\searchengineer\news_polity_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_polity_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_society_content.pk',
          r'D:\Github_project\data\searchengineer\news_society_X.pk',
          r'D:\Github_project\data\searchengineer\news_society_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_society_vectorized.pk')
    get_X(r'D:\Github_project\data\searchengineer\news_sports_content.pk',
          r'D:\Github_project\data\searchengineer\news_sports_X.pk',
          r'D:\Github_project\data\searchengineer\news_sports_word_2_id.pk',
          r'D:\Github_project\data\searchengineer\news_sports_vectorized.pk')