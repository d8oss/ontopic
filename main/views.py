from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Forums, Threads, Prefix, Icon, Post
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import string


def key(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


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
    comment = CommentForm()
    th = Threads.objects.filter(pk=th_id)
    po = Post.objects.filter(thid=th_id)
    context = {
        'th': th,
        'po': po,
        'form': comment
    }
    return render(request, 'main/threads.html', context)


def forum(request, fr_id):
    fr = Forums.objects.filter(pk=fr_id)
    th = Threads.objects.filter(forum=fr_id)
    context = {
        'fr': fr,
        'th': th
    }
    return render(request, 'main/byfr.html', context)


@login_required
def com(request, th_id):
    if request.method == "POST":
        content = request.POST.get("content")
        user = request.user.get_username()
        u = User.objects.get(username=user)
        post = Post(content=content, thid=th_id, user=u)
        post.save()
        return redirect('/threads/' + str(th_id) + '/#' + str(post.pk))
    else:
        return redirect('/')


@login_required
def create(request, fr_id):
    frget = Forums.objects.filter(pk=fr_id)
    context = {
        'fr': frget,
    }
    if request.method == "POST":
        # получаем юзера
        u = request.user.get_username()
        fr = Forums.objects.get(pk=fr_id)
        # получаем содержимое post запроса
        context = request.POST.get('content')
        title = request.POST.get('title')
        # создаем тему
        keyt = key(100)
        th = Threads(title=title, forum=fr, user=u, key=keyt)
        th.save()
        # получаем id созданной темы
        id = th.pk
        # создаем пост к теме
        post = Post(content=context, user=u, thid=id)
        post.save()
        return redirect('/threads/' + str(id) + '/')
    else:
        return render(request, 'main/create.html', context)


@login_required
def war(request, ps_id):
    ps = Post.objects.filter(pk=ps_id)
    context = {
        'ps': ps
    }
    if request.method == "POST":
        return HttpResponse('Спасибо! Ваша жалоба отправлена модераторам :)')
    else:
        return render(request, 'main/war.html', context)
