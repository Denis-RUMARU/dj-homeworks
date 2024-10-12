from django.http import HttpResponse
from django.shortcuts import render
import os
from datetime import datetime


def home_view(request):
    template_name = 'home.html'
    pages = {
        'Текущее время': 'current_time',
        'Рабочая директория': 'workdir',
    }
    context = {'pages': pages}
    return render(request, template_name, context)


def current_time_view(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(current_time)


def workdir_view(request):
    workdir = os.getcwd()
    files = os.listdir(workdir)
    return render(request, 'workdir.html', {'files': files})