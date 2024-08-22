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
    img_obj = {
        "img_list": [
            'img/choice/1-1.jpg',
            'img/choice/1-2.jpg',
            'img/choice/1-3.jpg',
            'img/choice/1-4.jpg',
        ]
    }
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def game2(request):
    img_obj = {
        "img_list": [
            'img/choice/2-1.jpg',
            'img/choice/2-2.jpg',
            'img/choice/2-3.jpg',
            'img/choice/2-4.jpg',
        ]
    }

    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def game3(request):
    img_obj = {
        "img_list": [
            'img/choice/3-1.jpg',
            'img/choice/3-2.jpg',
            'img/choice/3-3.jpg',
            'img/choice/3-4.jpg',
        ]
    }
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def game4(request):
    img_obj = {
        "img_list": [
            'img/choice/4-1.jpg',
            'img/choice/4-2.jpg',
            'img/choice/4-3.jpg',
            'img/choice/4-4.jpg',
        ]
    }
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

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