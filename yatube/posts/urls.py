from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список мороженого
    path('group_list/', views.group_list),
    # Подробная информация о мороженом. Ждем пременную типа int,
    # и будем использовать ее под именем pk
    path(
        'posts/<slug:slug>/',
        views.group_posts
    ),
]