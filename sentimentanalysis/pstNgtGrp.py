# coding: utf-8

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# https://www.kaggle.com/ngyptr/python-nltk-sentiment-analysis
import numpy as np # Numpyのインストール
import pandas as pd # Pandasのインストール
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets
# コーパス操作ライブラリのインストール
import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
# ワードクラウドのインストール
from wordcloud import WordCloud,STOPWORDS
# 以下はJupyterNotebook用
import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')
from subprocess import check_output

class PstNgtGrp:
    def pstNgtGrp(self):
        # PandasでCSVファイル読み込み
        data = pd.read_csv('sentiment.csv')
        # dataに格納
        data = data[['text','sentiment']]
        #print(data)
        # Splitting the dataset into train and test set
        train, test = train_test_split(data,test_size = 0.1)
        # Removing neutral sentiments
        train = train[train.sentiment != "neutral"]
        #print(train)
        # Positive、Negativeで扱うデータを分ける
        train_pos = train[ train['sentiment'] == 'positive']
        train_pos = train_pos['text']
        train_neg = train[ train['sentiment'] == 'negative']
        train_neg = train_neg['text']
        def wordcloud_draw(data, color = 'black'):
            words = ' '.join(data)
            cleaned_word = " ".join([word for word in words.split()
                                    if 'http' not in word
                                        and not word.startswith('@')
                                        and not word.startswith('#')
                                        and word != 'RT'
                                    ])
            wordcloud = WordCloud(stopwords=STOPWORDS,
                            background_color=color,
                            width=2500,
                            height=2000
                            ).generate(cleaned_word)
            if color =='white':
                str = 'positive'
            else:
                str = 'negative'
            # Wordcloud表示結果をPngファイルで出力
            wordcloud.to_file('wordcloud_' + str + '.png')
            # WordCloudは端末上で表示可能。ただし、処理時間が長いので割愛
            #lt.figure(1,figsize=(13, 13))
            #plt.imshow(wordcloud)
            #plt.axis('off')
            #plt.show()

        # 定義したモジュールの実行
        print("Positive words")
        wordcloud_draw(train_pos,'white')
        print("Positive words_file created")
        print("Negative words")
        wordcloud_draw(train_neg)
        print("Negative words_file created")
