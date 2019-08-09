# coding: utf-8
import MeCab # Mecabをインストール
import csv # CSVモジュールのインストール
import pandas as pd # Pandasのインストール
from sklearn.model_selection import train_test_split # function for splitting data to train and test sets

class SaLib:
    def saLib(self):
        #Pandas
        npen = pd.read_csv("pnendic.csv", sep = ':',names=('headword','pos', 'score')) #見出し語:品詞:感情極性実数値
        # 見出し語、スコアの変数を定義
        headword_column = npen['headword']
        score_column = npen['score']
        # 見出し語、スコアを列名に辞書作成
        npen_dic   = dict(zip(headword_column, score_column))
        # ScrapingしたCSVファイルを開く
        data = pd.read_csv('output.csv')
        # NaNが含まれるデータは行ごと削除
        data = data.dropna(how='any')
        # 必要な列だけ残し、dataに挿入
        data = data[['Num','Text']]
        # テキスト部分のみ変数Tweet1に挿入
        review_text = data['Text']
        # テキストと評判分析結果を格納するリスト変数を定義
        csvlist = [["text","sentiment"]]
        # テキスト部分をループ処理で取り出し
        for rt in review_text:
            tagger = MeCab.Tagger ("")
            kaisekiyou = rt.split('\r')
            string = ' '.join(kaisekiyou)
            mecab = tagger.parse(string)
            kaigyou = mecab.splitlines()
            #print(kaigyou)
            for tango_list in kaigyou:
                tab = tango_list.split('\t')
                #print(tab)
                if tab[0] in npen_dic:
                    pn_score = npen_dic[tab[0]]
                    sentiment = 'neutral'
                    # 数値０より大きいものをPositive、０未満をNegativeとラベル付け
                    if pn_score > 0:
                        sentiment = 'positive'
                    else:
                        sentiment = 'negative'
                    # 分割したテキストとラベルをリストに格納
                    csvlist.append([tab[0],sentiment])
                else:
                    pn_score = 'No words in dictionary'
                #print(pn_score)
                #print(csvlist)
        # CSVファイルを開く。ファイルがなければ新規作成する。
        f = open("sentiment.csv", "w")
        writecsv = csv.writer(f, lineterminator='\r')
        # 出力
        writecsv.writerows(csvlist)
        # CSVファイルを閉じる。
        f.close()
        print("SentimentAnalysis_Done")
