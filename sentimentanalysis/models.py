from django.db import models
from . import scrapingReview as sr
from . import saLib as sl
from . import pstNgtGrp as pn

# Create your models here.
class SentimentAnalysis(models.Model):
#    name = models.CharField("App", max_length=50)
#    done = models.BooleanField("完了")
#    created_at = models.DateTimeField(
#        "Created at",
#        auto_now_add=True)


#class Execution(models.Model):
    # Scrapingの呼び出し
#    url = input("Please enter URL:")
#    url = "https://www.yelp.com/biz/the-thonglor-san-francisco-2"
#    x = sr.Scraping()
    # ループで変数の数だけ呼び出す
#    x.scrUrl(url)
    # SentimentAnalysisの呼び出し
#    y = sl.SaLib()
#    y.saLib()
    # WordCloudを呼び出し
#    z = pn.PstNgtGrp()
#    z.pstNgtGrp()

    def __str__(self):
        return self.name
