from django.http import HttpResponse
from django.shortcuts import render
from . import scrapingReview as sr
from . import saLib as sl
from . import pstNgtGrp as pn
from .forms import IsValidForm

def index(request):
    return render(request, 'index.html')

def form_test(request):
    if request.method == "POST":
        form = IsValidForm(data=request.POST)  # ← 受け取ったPOSTデータを渡す
        if form.is_valid():  # ← 受け取ったデータの正当性確認
            pass  # ← 正しいデータを受け取った場合の処理
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        form = IsValidForm()
    return render(request, 'index.html', {
        'form': form,
    })

def result(request):
    # フォーム送信された値を受け取る
    result_num = request.POST.get('url')
    result_num2 = request.POST.get('url2')

#    if IsValidForm():
#        continue
#    else:
#        continue

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


    count += 1
    # ループで変数の数だけ呼び出す
    x.scrUrl(result_num2)
    # SentimentAnalysisの呼び出し
    y.saLib()
    # WordCloudを呼び出し
    z.pstNgtGrp(count)

    return render(request, 'result.html', {'url': result_num,
    'url2': result_num2})
