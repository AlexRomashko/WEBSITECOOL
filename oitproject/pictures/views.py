from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post, Category


cats_db = [
    {'id': 1, 'name': 'Кибербезопасность'},
    {'id': 2, 'name': 'Математика'},
    {'id': 3, 'name': 'Data Science'}
]


def index(request):
    return render(request, 'pictures/index.html')


def redirect_to_romashko(request):
    return redirect('romashko')


def about(request):
    return render(request, 'pictures/about.html')


def articles(request, cat_id):
    categories = Category.objects.all()
    if cat_id == 0:
        posts = Post.objects.all()  # Все посты
    else:
        posts = Post.objects.filter(cat_id=cat_id)
    data = {'posts': posts, 'cats_db': categories, 'active_cat': cat_id}
    return render(request, 'pictures/articles.html', context=data)


def show_post(request, post_id):
    posts = Post.objects.filter(id=post_id)
    data = {'posts': posts}
    return render(request, 'pictures/post.html', context=data)
