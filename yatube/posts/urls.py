from django.urls import path

from . import views

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список мороженого
    path('posts/', views.group_list),
    # Подробная информация о мороженом. Ждем пременную типа int,
    # и будем использовать ее под именем pk
    path(
        'posts/<slug:slug>/',
        views.group_posts
    ),
]