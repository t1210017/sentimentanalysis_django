from django.http import HttpResponse
from django.shortcuts import render
from . import scrapingReview as sr
from . import saLib as sl
from . import pstNgtGrp as pn

def index(request):
    return render(request, 'index.html')

def result(request):
    # フォーム送信された値を受け取る
    result_num = request.POST.get('url')
    x = sr.Scraping()
    # ループで変数の数だけ呼び出す
    x.scrUrl(result_num)
    # SentimentAnalysisの呼び出し
    y = sl.SaLib()
    y.saLib()
    # WordCloudを呼び出し
    z = pn.PstNgtGrp()
    z.pstNgtGrp()

    return render(request, 'result.html', {'url': result_num})
