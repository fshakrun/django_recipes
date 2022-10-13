import datetime
import os
import pathlib

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    # context и параметры render менять не нужно
    # подробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):

    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    files_list = []
    files = os.listdir()
    for file in files:
        files_list.append(f'\n {file}')
    return HttpResponse(files_list)
