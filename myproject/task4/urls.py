# task4/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),  # Глава страница
    path('games/',views.games, name='games'),  # Вторая страница
    path('about/', views.about, name='about'),  # Третья страница
]