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
    result_num2 = request.POST.get('url2')

    count = 0
    x = sr.Scraping()
    # ループで変数の数だけ呼び出す
    x.scrUrl(result_num)
    # SentimentAnalysisの呼び出し
    y = sl.SaLib()
    y.saLib()
    # WordCloudを呼び出し
    z = pn.PstNgtGrp()
    z.pstNgtGrp(count)

    if result_num2 != "":
        count += 1
        # ループで変数の数だけ呼び出す
        x.scrUrl(result_num2)
        # SentimentAnalysisの呼び出し
        y.saLib()
        # WordCloudを呼び出し
        z.pstNgtGrp(count)

        return render(request, 'result2.html', {'url': result_num,
        'url2': result_num2})

    return render(request, 'result.html', {'url': result_num})
