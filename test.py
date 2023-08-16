import sklearn.feature_extraction.text as ft
import nltk.tokenize as tk
import pandas as pd
from tqdm import tqdm
from test_jieba import *


if __name__ == '__main__':

      # 读取点评数据
      df_raw = pd.read_csv('dataset_train.csv', sep=',', header=0, index_col=0)
      print('Data loaded with', len(df_raw), 'records.')
 
      searchfor = ['工商银行','农业银行','建设银行','中国银行','交通银行','招商银行']
      mask1 = df_raw['text'].str.contains('|'.join(searchfor))
      mask2 = ~df_raw['text'].str.contains('IMG')
      df_review = df_raw[mask1][mask2][['text']]
      df_review.columns = ['review']

      # 进行结巴分词
      review = '.'.join(df_review.review)
      result = stripdata(review).split('/')

      # # 计算每个关键词出现的频率
      # for item in result:
      #       df_review[item]= df_review.review.str.contains(item)#.astype(int)

      for item1 in tqdm(result):
            for item2 in result:
                  if item1 not in item2 and item2 not in item1 :
                        # 包含item1的记录数
                        ct1 = sum(df_review.review.str.contains(item1))
                        # 包含item2的记录数
                        ct2 = sum(df_review.review.str.contains(item1))
                        # 同时包含item1和item2的记录数
                        ct12 = sum(df_review.review.str.contains(item1) & df_review.review.str.contains(item2))
                        # P(w2|w1)
                        p21 = round(ct12/ct1, 4)
                        # P(w2|not w1)
                        p2n1 = round((ct2-ct12)/(50-ct1), 4)

                        # item1出现时有超过一半的概率item2出现
                        # 且item1不出现时item2几乎不出现
                        if p21>0.5 and p2n1<0.01 and ct1>5:
                              print('\n')
                              print(item1, ct1)
                              print(item2, ct12)
                              print('P(W2|W1):', p21)
                              print(item1, '未出现', 50-ct1)
                              print(item2, ct2-ct12)
                              print('P(W2|notW1):', p2n1)
