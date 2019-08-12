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
        # Positive, Negative、その合計の件数を取得
        pos_count = train_pos.count()
        neg_count = train_neg.count()
        pos_nega_totalcount = pos_count + neg_count
        print("Posi Num:" + str(pos_count))
        print("Nega Num:" + str(neg_count))
        print("Posi, Nega Total is:" + str(pos_nega_totalcount))
        print("Posi ratio is:" + str(pos_count/pos_nega_totalcount))
        posi_percentage = '{:.0%}'.format(pos_count/pos_nega_totalcount)
        print("Posi percentage is:" + posi_percentage)
        nega_percantage = '{:.0%}'.format(neg_count/pos_nega_totalcount)
        print("Nega percentage is:" + nega_percantage)
        # WordCloudの高さ、幅を比率によって決定する
        pos_ratio = pos_count/pos_nega_totalcount
        neg_ratio = neg_count/pos_nega_totalcount
        if pos_count > neg_count:
            pos_ratio += 0.1
            neg_ratio -+ 0.1
        else:
            pos_ratio -= 0.1
            neg_ratio += 0.1
        pos_width = int(round(2000 * pos_ratio))
        pos_height = int(round(1600 * pos_ratio))
        neg_width = int(round(2000 * neg_ratio))
        neg_height = int(round(1600 * neg_ratio))
        print("Pos width" + str(pos_width) + "Pos height" + str(pos_height))
        def wordcloud_draw(data, color = 'black'):
            words = ' '.join(data)
            cleaned_word = " ".join([word for word in words.split()
                                    if 'http' not in word
                                        and not word.startswith('@')
                                        and not word.startswith('#')
                                        and word != 'RT'
                                    ])
            # Positive, Negativeにより出力サイズを分ける
            if color =='white':
                str = 'positive'
                wordcloud = WordCloud(stopwords=STOPWORDS,
                background_color=color,
                width=pos_width,
                height=pos_height
                ).generate(cleaned_word)
            else:
                str = 'negative'
                wordcloud = WordCloud(stopwords=STOPWORDS,
                background_color=color,
                width=neg_width,
                height=neg_height
                ).generate(cleaned_word)
            # Wordcloud表示結果をPngファイルで出力
            #wordcloud.to_file('wordcloud_' + str + '.png')
            wordcloud.to_file('./sentimentanalysis/static/images/wordcloud_' + str + '.png')
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
