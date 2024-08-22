from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def lobby(request):
    template = loader.get_template('lobby.html')
    return HttpResponse(template.render())

def video(request):
    template = loader.get_template('video.html')
    return HttpResponse(template.render())

def game1(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render())

def game2(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render())

def game3(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render())

def game4(request):
    template = loader.get_template('game.html')
    return HttpResponse(template.render())

def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render())

def detail(request):
    template = loader.get_template('user/detail.html')
    return HttpResponse(template.render())

def info(request):
    template = loader.get_template('user/info.html')
    return HttpResponse(template.render())

def outcome(request):
    template = loader.get_template('user/outcome.html')
    return HttpResponse(template.render())

def bet(request):
    template = loader.get_template('user/bet.html')
    return HttpResponse(template.render())

def notice(request):
    template = loader.get_template('user/notice.html')
    return HttpResponse(template.render())

def contact(request):
    template = loader.get_template('user/contact.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login/login.html')
    return HttpResponse(template.render())

def register(request):
    template = loader.get_template('login/register.html')
    return HttpResponse(template.render())