from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import *
from . import models
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
import requests
import time

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
            {"img": 'img/choice/1-1.jpg',
            "des": 'Combo 1'},
            {"img": 'img/choice/1-2.jpg',
            "des": 'Combo 2'},
            {"img": 'img/choice/1-3.jpg',
            "des": 'Combo 3'},
            {"img": 'img/choice/1-4.jpg',
            "des": 'Combo 4'}
        ],
    }
    customer = request.user.username
    if customer:
        member = models.Member.objects.get(username=customer)
        img_obj["member"] = member
    img_obj["current"] = requests.get('http://127.0.0.1:8000/lottery/current?id=1').json()["data"][0][0]
    img_obj["last"] = requests.get('http://127.0.0.1:8000/lottery/last?id=1').json()["data"][9]
    img_obj["last"]['opencode'] = (img_obj["last"]['opencode']).replace('1', 'Combo 1').replace('2', 'Combo 2').replace('3', 'Combo 3').replace('4', 'Combo 4')
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def game2(request):
    img_obj = {
        "img_list": [
            {"img": 'img/choice/2-1.jpg',
            "des": 'Combo 1'},
            {"img": 'img/choice/2-2.jpg',
            "des": 'Combo 2'},
            {"img": 'img/choice/2-3.jpg',
            "des": 'Combo 3'},
            {"img": 'img/choice/2-4.jpg',
            "des": 'Combo 4'}
        ]
    }
    customer = request.user.username
    if customer:
        member = models.Member.objects.get(username=customer)
        img_obj["member"] = member
    img_obj["current"] = requests.get('http://127.0.0.1:8000/lottery/current?id=2').json()["data"][0][0]
    img_obj["last"] = requests.get('http://127.0.0.1:8000/lottery/last?id=2').json()["data"][9]
    img_obj["last"]['opencode'] = (img_obj["last"]['opencode']).replace('1', 'Combo 1').replace('2', 'Combo 2').replace('3', 'Combo 3').replace('4', 'Combo 4')
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def game3(request):
    img_obj = {
        "img_list": [
            {"img": 'img/choice/3-1.jpg',
            "des": 'Combo 1'},
            {"img": 'img/choice/3-2.jpg',
            "des": 'Combo 2'},
            {"img": 'img/choice/3-3.jpg',
            "des": 'Combo 3'},
            {"img": 'img/choice/3-4.jpg',
            "des": 'Combo 4'}
        ]
    }
    customer = request.user.username
    if customer:
        member = models.Member.objects.get(username=customer)
        img_obj["member"] = member
    img_obj["current"] = requests.get('http://127.0.0.1:8000/lottery/current?id=3').json()["data"][0]
    img_obj["last"] = requests.get('http://127.0.0.1:8000/lottery/last?id=3').json()["data"][9]
    img_obj["last"]['opencode'] = (img_obj["last"]['opencode']).replace('1', 'Combo 1').replace('2', 'Combo 2').replace('3', 'Combo 3').replace('4', 'Combo 4')
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def game4(request):
    img_obj = {
        "img_list": [
            {"img": 'img/choice/4-1.jpg',
            "des": 'Combo 1'},
            {"img": 'img/choice/4-2.jpg',
            "des": 'Combo 2'},
            {"img": 'img/choice/4-3.jpg',
            "des": 'Combo 3'},
            {"img": 'img/choice/4-4.jpg',
            "des": 'Combo 4'}
        ]
    }
    customer = request.user.username
    if customer:
        member = models.Member.objects.get(username=customer)
        img_obj["member"] = member
    img_obj["current"] = requests.get('http://127.0.0.1:8000/lottery/current?id=4').json()["data"][0]
    img_obj["last"] = requests.get('http://127.0.0.1:8000/lottery/last?id=4').json()["data"][9]
    img_obj["last"]['opencode'] = (img_obj["last"]['opencode']).replace('1', 'Combo 1').replace('2', 'Combo 2').replace('3', 'Combo 3').replace('4', 'Combo 4')
    template = loader.get_template('game.html')
    return HttpResponse(template.render(img_obj, request))

def account(request):
    customer = request.user.username
    if customer:
        member = models.Member.objects.get(username=customer)
        print(member)
    if customer == None:
        print("check")
    print(customer)
    context = {
        "name": customer,
        "wallet": "123",
    }
    if customer:
        context['member'] = member
    return render(request, "account.html", context)

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

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            print(username, password)
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "login/login.html", {"form": form, "msg": msg})


def register_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            member = models.Member(
                username = form.cleaned_data.get("username"),
                password = form.cleaned_data.get("password1"),
                status = 1,
                money = 0,
                amount_code = 3,
                phone = "",
                name = form.cleaned_data.get("username"),
                sex = "Chưa xác định",
                paypassword = "",
                header_img = "",
                uid = form.cleaned_data.get("uid"),
                update_time = 0,
                ip = "Không xác định",
                num = 1000,
                min = 100,
                max = 1000000000000,
                is_online = 0,
                role = 0,
                area = "",
                daili = form.cleaned_data.get("uid"),
            )
            member.save()
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Tạo tài khoản thành công <br> Mời bạn <a href="/login">Đăng nhập</a>.'
            success = True
        else:
            msg = form.errors.as_text
    else:
        form = SignUpForm()

    return render(request, "login/register.html", {"form": form, "msg": msg, "success": success})
