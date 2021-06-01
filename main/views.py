from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Forums, Threads, Prefix, Icon, Post, Users
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import string
from django.contrib.auth.forms import UserCreationForm


def key(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def index(request):
    us = Users.objects.all()[:3]
    th = Threads.objects.all()
    fr = Forums.objects.all()
    pr = Prefix.objects.all()
    ic = Icon.objects.all()
    context = {
        'th': th,  # темы
        'fr': fr,  # разделы
        'pr': pr,  # префиксы
        'ic': ic,  # иконки
        'us': us,
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
    po = Post.objects.filter(thid=th_id)[:10]
    context = {
        'th': th,
        'po': po,
        'form': comment
    }
    if not th:
        return redirect('/')
    else:
        return render(request, 'main/threads.html', context)


def forum(request, fr_id):
    fr = Forums.objects.filter(pk=fr_id)
    th = Threads.objects.filter(forum=fr_id)
    context = {
        'fr': fr,
        'th': th
    }
    if not fr:
        return redirect('/')
    else:
        return render(request, 'main/byfr.html', context)


@login_required
def com(request, th_id):
    if request.method == "POST":
        content = request.POST.get("content")
        user = request.user.get_username()
        u = Users.objects.get(user=user)
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
        user = Users.objects.get(user=u)
        fr = Forums.objects.get(pk=fr_id)
        # получаем содержимое post запроса
        context = request.POST.get('content')
        title = request.POST.get('title')
        # создаем тему
        keyt = key(100)
        th = Threads(title=title, forum=fr, user=user, key=keyt)
        th.save()
        # получаем id созданной темы
        id = th.pk
        # создаем пост к теме
        post = Post(content=context, user=user, thid=id)
        post.save()
        return redirect('/threads/' + str(id) + '/')
    else:
        if not frget:
            return redirect('/')
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


def user(request, us_nik):
    u = Users.objects.filter(user=us_nik)
    u2 = Users.objects.get(user=us_nik)
    posts = Post.objects.filter(user=u2).count()
    threads = Threads.objects.filter(user=u2).count()
    if not u:
        return redirect('/')
    else:
        context = {
            'u': u,
            'p': posts,
            't': threads,
        }
        return render(request, 'main/user.html', context)


@login_required
def like(request, post_id):
    posts = Post.objects.get(pk=post_id)
    posts.like += 1
    posts.save()
    return HttpResponse('Ок')


def reg(request):
    data = {}
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()

            u = request.POST.get('username')

            user = Users(user=u)

            user.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return HttpResponse('Отлично! Теперь вам нужно <a href="/accounts/login">войти</a> на форум.')
    else:  # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'main/reg.html', data)
