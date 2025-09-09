"""
URL configuration for minijogopy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django_distill import distill_path
from game.views import game_view

def get_choices():
    # Lista de escolhas para gerar páginas estáticas
    for choice in ['rock', 'paper', 'scissors']:
        yield {'choice': choice}

urlpatterns = [
    path("admin/", admin.site.urls),
    distill_path(
        '',
        game_view,
        name='game',
        distill_func=lambda: [{}],  # sem parâmetro
        distill_file='index.html'
    ),
    distill_path(
        '<str:choice>/',
        game_view,
        name='game_choice',
        distill_func=get_choices,
        distill_file='{choice}.html'
    ),
]
