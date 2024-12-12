"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import FeedbackForm, BootstrapAuthenticationForm
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm
import logging
from django.db import models
from .models import Blog
from .models import Comment 
from .forms import CommentForm
from .forms import BlogForm
from .models import VideoGame
from django.db.models import Q
from .models import VideoGame, Genre
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
logger = logging.getLogger(__name__)



def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная страница',
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
            'message':'Ваша страница контактов.',
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
            'title':'О нас',
            'message':'Страница описания вашего приложения.',
            'year':datetime.now().year,
        }
    )
def news(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/news.html',
        {
            'title':'Новости',
            'message':'Новости о последних игра.',
            'year':datetime.now().year,
        }
    )

def feedback(request):
    assert isinstance(request, HttpRequest)
    data = None
    average_rating = None  # Инициализация переменной

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            # Обработка данных формы
            data['nickname'] = form.cleaned_data['nickname']
            data['game'] = form.cleaned_data['game']
            data['speed'] = form.cleaned_data['speed']
            data['price'] = form.cleaned_data['price']
            data['service'] = form.cleaned_data['service']
            data['message'] = form.cleaned_data['message']

            # Вычисление средней оценки
            average_rating = round((int(data['speed']) + int(data['price']) + int(data['service'])) / 3, 1)

            form = None
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = FeedbackForm()

    return render(
        request,
        'app/feedback.html',
        {
            'form': form,
            'data': data,
            'average_rating': average_rating,
            'year': datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""

    if request.method == "POST":  # после отправки формы
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False  # запрещен вход в админ. раздел
            reg_f.is_active = True  # активный пользователь
            reg_f.is_superuser = False  # не является суперпользователем
            reg_f.date_joined = datetime.now()  # дата регистрации
            reg_f.last_login = datetime.now()  # дата последней авторизации

            regform.save()  # сохраняем изменения после добавления полей

            return redirect('home')  # переадресация на главную страницу после авторизации
        else:
            return render(
                request,
                'app/registration.html',
                {
                    'regform': regform,
                    'year': datetime.now().year,
                }
            )
    else:
        regform = UserCreationForm()  # создание объекта формы для ввода данных
        return render(
            request,
            'app/registration.html',
            {
                'regform': regform,
                'year': datetime.now().year,
            }
        )

def blog(request):
    """Renders the blog page."""

    posts = Blog.objects.all()  # запрос на выбор всех статей блога из модели

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог:',
            'posts': posts,  # передача списка статей в шаблон веб-страницы
            'year': datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
   
    post_1 = Blog.objects.get(id=parametr) 

    # Получаем комментарии для данного поста
    comments = Comment.objects.filter(post=post_1)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()
            comment_f.post = post_1
            comment_f.save()

            return redirect('blogpost', parametr=post_1.id)
    else:
        form = CommentForm()  # Инициализация формы для GET-запросов

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,  # передача конкретной статьи в шаблон веб-страницы
            'comments': comments,
            'form': form,
            'year': datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)

    if request.method == 'POST':
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()

    return render(
       request,
        'app/newpost.html',
        {
            'blogform': blogform,
            'title': 'Добавить статью блога',

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
            'title':'Видео:',
            'year':datetime.now().year,
        }
    )


def videogame_list(request):
    query = request.GET.get('q')
    genre = request.GET.get('genre')
    games = VideoGame.objects.all()

    if query:
        games = games.filter(Q(title__icontains=query))

    if genre:
        games = games.filter(Q(genres__name__icontains=genre))

    genres = Genre.objects.all()
    return render(request, 'app/videogame_list.html', {'games': games, 'genres': genres})

def videogame_detail(request, parametr):
    game = get_object_or_404(VideoGame, id=parametr)
    return render(request, 'app/videogame_detail.html', {'game': game})

@login_required
def add_to_cart(request, game_id):
    game = get_object_or_404(VideoGame, id=game_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, game=game)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'app/cart_detail.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})
@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'app/checkout.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})

@require_POST
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')

def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    return render(request, 'app/cart.html', {'cart_items': cart_items, 'total_price': total_price})


