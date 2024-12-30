# task4/views.py

from django.shortcuts import render

def menu(request):
    return render(request, 'menu.html')

def games(request):
       return render(request, 'games.html')

def about(request):
    return render(request, 'about.html')


def games(request):
       # Пример списка игр
    games_list = ['Atomic War', 'Cyberpunk2', 'Мир танков']
    return render(request, 'games.html', {'games': games_list})
