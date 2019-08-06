"""mi_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from . import views
import re


app_name = 'sea_battle'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new_registration_attempt', views.registration, name='registration'),
    path('new_log_in_attempt', views.log_in, name='log_in'),
    re_path(r'id\d+/personal_area/', views.personal_area, name='personal_area'),
    path('change_username', views.change_username, name='change_username'),
    path('change_password', views.change_password, name='change_password'),
    path('delete_player', views.delete_player, name='delete_player'),
    path('log_out', views.log_out, name='log_out'),
    path('start_game', views.start_game, name='start_game'),
    re_path(r'id\d+/start_game/', views.game_choice, name='game_choice'),
    path('statistic', views.statistic, name='statistic'),
    re_path(r'id\d+/statistic/', views.statistic_choice, name='statistic_choice'),
    path('result_of_searching', views.search, name='search'),
    path('return_to_personal_area', views.return_to_personal_area, name='return_to_personal_area'),


    path('game/', views.GameView.as_view(), name='game'),

]
