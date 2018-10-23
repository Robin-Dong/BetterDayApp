from django.shortcuts import render, get_object_or_404,redirect
from . import models
import ast
from . import monitors

# Create your views here.


def home(request):
    daily_en = models.DailyEnglish.objects.all().last()
    daily_img = models.DailyImg.objects.all().last()
    daily_quote = models.DailyQuote.objects.all().last()
    a = daily_en.pic_url
    daily_en.pic_url = ast.literal_eval(a)
    return render(request, 'daily_english/index.html', locals())


def permission_denied(request):
    '''403'''
    return render(request, 'daily_english/403.html', locals())


def page_not_found(request):
    '''404'''
    return render(request, 'daily_english/404.html', locals())


def page_error(request):
    '''500'''
    return render(request, 'daily_english/500.html', locals())