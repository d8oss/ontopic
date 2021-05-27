from django.shortcuts import render
from django.http import HttpResponse
from .models import Forums, Threads, Prefix, Icon, Post


def index(request):
    th = Threads.objects.all()
    fr = Forums.objects.all()
    pr = Prefix.objects.all()
    ic = Icon.objects.all()
    context = {
        'th': th,  # темы
        'fr': fr,  # разделы
        'pr': pr,  # префиксы
        'ic': ic,  # иконки
    }
    return render(request, 'main/index.html', context)


def forums(request):
    fr = Forums.objects.all()
    context = {
        'fr': fr
    }
    return render(request, 'main/forums.html', context)


def thread(request, th_id):
    th = Threads.objects.filter(pk=th_id)
    po = Post.objects.filter(thid=th_id)
    context = {
        'th': th,
        'po': po
    }
    return render(request, 'main/threads.html', context)
