# coding: utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import math

class Scraping():
      def scrUrl(self,url):
          response = requests.get(url)
          response.encoding = response.apparent_encoding
          # Beautiful Soupに取得したHTMLのテキストデータを代入
          bs = BeautifulSoup(response.text, 'html.parser')
          # Csv構築用のリスト型変数を定義、リスト番号Numを０から定義
          csvlist = [["Num","Text"]]
          num = 0
          # 「p」タグのデータ＝中身のテキストを取得
          for i in bs.select("p"):
              text = i.getText()
              text = text.strip()
              # Nullデータはパスする
              if len(str(text)) ==0:
                  continue
              else:
                  csvlist.append([num,text])
              # NaN（浮動小数）のカットは変数定義上できなかった
              #if math.isnan(int(text)):
                #  continue
              #else:
                #  csvlist.append([num,text])
              num += 1
          # CSVファイルを開く。ファイルがなければ新規作成する。
          f = open("output.csv", "w")
          writecsv = csv.writer(f, lineterminator='\r')
          # 出力
          writecsv.writerows(csvlist)
          # CSVファイルを閉じる
          f.close()
          print("ScrapingReview_Done")
