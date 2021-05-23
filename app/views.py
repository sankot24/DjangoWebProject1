"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import AnketaTest
from django.db import models

from datetime import datetime

from .models import Comment
from .forms import CommentForm

from .models import Blog
from .forms import BlogForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты',
            'message':'Контакты.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'Обо мне',
            'message':'Немного',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    """Renders the anketa page."""
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1' : 'М', '2' : 'Ж', '3' : 'Не указано'}
    play = {'1': 'Цветовая гамма', '2': 'Тематика блога', '3': 'Стиль написания текста',
                                       '4': 'Все перечисленное'}
    if request.method == 'POST':
        form = AnketaTest(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']

            data['gender'] = gender[form.cleaned_data['gender']]
            data['play'] = play[form.cleaned_data['play']]
            data['email'] = form.cleaned_data['email']

            if (form.cleaned_data['like'] == True):
                data['like'] = 'Да'
            else:
                data['like'] = 'Нет'

            data['message'] = form.cleaned_data['message']
            form = None
    else:
       form = AnketaTest()
    return render(
           request,
           'app/anketa.html',
          {
               'title':'Обратная связь',
               'form':form,
               'data':data
           }
       )

def registration(request):
    """Renders the registration page."""
    if request.method == "POST":
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()

            regform.save()
            return redirect('home')
    else:
        regform = UserCreationForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {
            'title':'Регистрация',
            'regform': regform,

            'year': datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.all()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts,
            'year': datetime.now().year,
            
        }
    )

 
def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id = parametr)
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            commert_f = form.save(commit=False)
            commert_f.author = request.user
            commert_f.date = datetime.now()
            commert_f.post = Blog.objects.get(id=parametr)
            
            commert_f.save()
            return redirect('home')
    else:
        form = CommentForm()


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'title':'Пост',
            'post_1': post_1,
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )
 
def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user

            if 'image' in request.FILES:
                blog_f.image = request.FILES['image']

            blog_f.save()
            return redirect('blog')
    else:
        blogform = BlogForm()

    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': "Добавьте статью блога",
            'year': datetime.now().year,
        }
    )
 
def videopost(request):
    """Renders the videopost page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видосики',
            'year': datetime.now().year,
        }
    )
def res(request):
    """Renders the res page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/res.html',
        {
            'title':'Полезные ресурсы',
            'year':datetime.now().year,
        }
    )