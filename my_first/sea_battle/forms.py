from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Player
from datetime import datetime


class PlayerRegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=30, min_length=5)
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput)

    def check(self):
        self.is_valid()
        try:
            username = self.cleaned_data['username']
        except KeyError:
            return False, "Your username must be from 5 to 30 symbols. Try another name."
        try:
            password = self.cleaned_data['password']
        except KeyError:
            return False, "Your password must be less then 31 symbols. Try another password."
        user_list = User.objects.filter(username=username)
        if user_list:
            return False, "This name is already taken. Try another name."
        user = User.objects.create_user(username=username, password=password)
        user.save()
        new_player = Player(username=username, registration_date=datetime.now(), last_connection_date=datetime.now())
        new_player.save()
        return new_player.id, ''


class PlayerLogInForm(forms.Form):
    username = forms.CharField(label='username', max_length=30, min_length=5)
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput)

    def check(self):
        self.is_valid()
        try:
            username, password = self.cleaned_data['username'], self.cleaned_data['password']
        except KeyError:
            return False, "Your username must be from 5 to 30 symbols. Try another name."
        player = Player.objects.filter(username=username)
        if not player:
            return False, "User doesn't exist. Check the entered name."
        data = authenticate(username=username, password=password)
        if not data:
            return False, "Wrong username or password. Please, check and enter again."
        player[0].last_connection_date = datetime.now()
        player[0].save()
        return player[0].id, ''


class ChangeUsername(forms.Form):
    old_username = forms.CharField(label='username', max_length=30, min_length=5)
    new_username = forms.CharField(label='new_username', max_length=30, min_length=5)
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput)

    def check(self):
        self.is_valid()
        try:
            old_username = self.cleaned_data['old_username']
            new_username = self.cleaned_data['new_username']
            password = self.cleaned_data['password']
            print(old_username, new_username, password)
        except KeyError:
            return "Your new username must be from 5 to 30 symbols. Try another name."
        player = Player.objects.filter(username=new_username)
        if player:
            return "Your new username already exist. Try another name."
        player = Player.objects.get(username=old_username)
        user = User.objects.get(username=old_username)
        data = authenticate(username=player.username, password=password)
        player.username = new_username
        player.last_connection_date = datetime.now()
        player.save()
        user.username = new_username
        user.save()
        if not data:
            return "Wrong password. Please, check and enter again."
        return ''


class ChangePassword(forms.Form):
    old_username = forms.CharField(label='old_username', max_length=30, min_length=5)
    old_password = forms.CharField(label='old_password', max_length=30, widget=forms.PasswordInput)
    new_password = forms.CharField(label='new_password', max_length=30, widget=forms.PasswordInput)
    new_password_again = forms.CharField(label='new_password_again', max_length=30, widget=forms.PasswordInput)

    def check(self):
        self.is_valid()
        print(self.cleaned_data['old_username'], self.cleaned_data['old_password'],
              self.cleaned_data['new_password'], self.cleaned_data['new_password_again'])
        try:
            old_username = self.cleaned_data['old_username']
            old_password = self.cleaned_data['old_password']
            new_password = self.cleaned_data['new_password']
            new_password_again = self.cleaned_data['new_password_again']
        except KeyError:
            return "Your password must be less then 31 symbols. Try another password."
        data = authenticate(username=old_username, password=old_password)
        if not data:
            return "Wrong password. Please, check and enter again."
        if old_password == new_password:
            return "Your new password can't be the same as old password. Try another password."
        if new_password != new_password_again:
            return "New password does not match. Please, check and enter again."
        user = User.objects.get(username=old_username)
        user.set_password(new_password)
        user.save()
        return ''


class DeletePlayer(forms.Form):
    old_username = forms.CharField(label='old_username', max_length=30, min_length=5)
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput)

    def check(self):
        self.is_valid()
        print(self.cleaned_data['old_username'], self.cleaned_data['password'])
        try:
            old_username = self.cleaned_data['old_username']
            password = self.cleaned_data['password']
        except KeyError:
            return "Your password must be less then 31 symbols. Try another name."
        data = authenticate(username=old_username, password=password)
        if not data:
            return "Wrong password. Please, check and enter again."
        User.objects.get(username=old_username).delete()
        return ''


class Statistic(forms.Form):
    username = forms.CharField(label='username', max_length=30, min_length=5)
    games = forms.RadioSelect()
    won_games = forms.RadioSelect()
    percent = forms.RadioSelect()
    registration = forms.RadioSelect()
    connection = forms.RadioSelect()
    sorting_by = forms.RadioSelect()

    def check(self):
        self.is_valid()
        print(self)
        try:
            username = self.cleaned_data['username']
            return username, ''
        except KeyError:
            return False, "Username must be from 5 to 30 symbols. Try another name."

