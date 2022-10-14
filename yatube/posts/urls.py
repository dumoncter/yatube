from django.urls import path

from . import views
app_name = 'posts'

app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='main'),
    # Список групп
    path('group_list/', views.group_list, name='group_list'),
    path(
        'posts/<slug:slug>/',
        views.group_posts
    ),
]