from django.urls import path
from . import views
from django.shortcuts import render, redirect

urlpatterns = [
    path('', views.redirect_to_romashko),
    path('romashko', views.index, name='romashko'),
    path('articles/<int:cat_id>/', views.articles, name='articles'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('about', views.about, name='about')
]
