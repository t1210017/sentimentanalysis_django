from django.shortcuts import render
from django.http import HttpResponse
from .models import SentimentAnalysis

def index(request):
    #return render("Hello")
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
