import sklearn.feature_extraction.text as ft
import nltk.tokenize as tk
# https://blog.csdn.net/weixin_45081640/article/details/118109647

doc = 'Researchers at Harvard University\'s School of Public ' \
      'Health in Boston did the study. They compared women ' \
      'with "a general expectation that good things will happen' \
      '" to women who were less optimistic. They found that the ' \
      'optimists had a much lower risk of getting several deadly' \
      ' diseases, including cancer, heart disease, stroke, ' \
      'respiratory disease and certain types of infection.'

# 拆分句子
sents = tk.sent_tokenize(doc)
print(sents)

# 构建词袋模型
model = ft.CountVectorizer()
bow = model.fit_transform(sents)
print(bow.toarray())
print(model.get_feature_names())