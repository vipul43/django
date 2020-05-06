from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getTime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
