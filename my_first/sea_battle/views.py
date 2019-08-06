from django.shortcuts import render, redirect
from django.views import generic
from .models import Player
from .forms import *
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.base import SessionBase
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'sea_battle/index.html'
    model = Player


class GameView(generic.ListView):
    template_name = 'sea_battle/game.html'
    model = Player
    ...


def registration(request):
    if request.method == "POST":
        new_player_id, mistake = PlayerRegistrationForm(request.POST).check()
        if mistake:
            return render(request, 'sea_battle/index.html', {'mistake': mistake})
        request.session['id'] = new_player_id
        return redirect('id{}/personal_area/'.format(new_player_id))
    else:
        return render(request, 'sea_battle/index.html', {'mistake': "Wrong request method."})


def personal_area(request):
    return render(request, 'sea_battle/personal_area.html', {'info': Player.objects.get(id=request.session['id'])})


def log_in(request):
    if request.method == "POST":
        player_id, mistake = PlayerLogInForm(request.POST).check()
        if mistake:
            return render(request, 'sea_battle/index.html', {'mistake': mistake})
        request.session['id'] = player_id
        return redirect('id{}/personal_area/'.format(player_id))
    else:
        return render(request, 'sea_battle/index.html', {'mistake': "Wrong request method."})


def change_username(request):
    if request.method == "POST":
        form = ChangeUsername(request.POST)
        mistake = form.check()
        player = Player.objects.get(id=request.session['id'])
        if mistake:
            return render(request, 'sea_battle/personal_area.html',
                          {'mistake': mistake, 'info': player})
        return redirect('id{}/personal_area/'.format(player.id))
    else:
        player = Player.objects.get(id=request.session['id'])
        return render(request, 'sea_battle/personal_area.html',
                      {'mistake': 'Wrong request method.', 'info': player})


def change_password(request):
    if request.method == "POST":
        mistake = ChangePassword(request.POST).check()
        player = Player.objects.get(id=request.session['id'])
        if mistake:
            return render(request, 'sea_battle/personal_area.html',
                          {'mistake': mistake, 'info': player})
        return redirect('id{}/personal_area/'.format(player.id))
    else:
        player = Player.objects.get(id=request.session['id'])
        return render(request, 'sea_battle/personal_area.html',
                      {'mistake': 'Wrong request method.', 'info': player})


def delete_player(request):
    if request.method == "POST":
        mistake = DeletePlayer(request.POST).check()
        if mistake:
            player = Player.objects.get(id=request.session['id'])
            return render(request, 'sea_battle/personal_area.html',
                          {'mistake': mistake, 'info': player})
        log_out(request)
    else:
        player = Player.objects.get(id=request.session['id'])
        return render(request, 'sea_battle/personal_area.html',
                      {'mistake': 'Wrong request method.', 'info': player})


def log_out(request):
    del request.session['id']
    return redirect(reverse('sea_battle:index'))


def start_game(request):
    if request.method == "POST":
        player = Player.objects.get(id=request.session['id'])
        return redirect('id{}/start_game/'.format(player.id))
    else:
        player = Player.objects.get(id=request.session['id'])
        return render(request, 'sea_battle/personal_area.html',
                      {'mistake': "Wrong request method.", 'info': player})


def game_choice(request):
    return render(request, 'sea_battle/game_choice.html', {'info': Player.objects.get(id=request.session['id'])})


def statistic(request):
    if request.method == "POST":
        player = Player.objects.get(id=request.session['id'])
        return redirect('id{}/statistic/'.format(player.id))
    else:
        player = Player.objects.get(id=request.session['id'])
        return render(request, 'sea_battle/personal_area.html',
                      {'mistake': "Wrong request method.", 'info': player})


def statistic_choice(request):
    return render(request, 'sea_battle/statistics_choice.html', {'info': Player.objects.get(id=request.session['id'])})


def search(request):
    if request.method == "POST":
        username, mistake = Statistic(request.POST).check()
        if mistake:
            return render(request, 'sea_battle/statistics_choice.html',
                          {'mistake': mistake})
        sorting_by = request.POST['sorting_by']
        if username != "None name":
            result = Player.objects.filter(username=username)
            if result:
                return render(request, 'sea_battle/statistics_choice.html',
                              {'list_of_player_statistics': result})
            else:
                return render(request, 'sea_battle/statistics_choice.html',
                              {'mistake': "User with this name doesn't exist."})
        if request.POST[sorting_by] == 'ascending':
            result = Player.objects.all().order_by(sorting_by)[:20]
        else:
            result = Player.objects.all().order_by('-' + sorting_by)[:20]
        return render(request, 'sea_battle/statistics_choice.html',
                      {'list_of_player_statistics': result})
    else:
        return render(request, 'sea_battle/statistics_choice.html',
                      {'mistake': "Wrong request method."})


def return_to_personal_area(request):
    player = Player.objects.get(id=request.session['id'])
    return redirect('id{}/personal_area/'.format(player.id))

