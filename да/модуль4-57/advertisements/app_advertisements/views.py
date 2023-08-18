from django.shortcuts import render
from django.http import HttpResponse

from .models import Advertisement


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'word': 'hello world'}
    return render(request, "index.html", context = context)


def top_sellers(request):
    return render(request, "top-sellers.html")
