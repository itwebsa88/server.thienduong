from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lobby/', views.lobby, name='lobby'),
    path('video/', views.video, name='video'),
    path('game/1/', views.game1, name='game1'),
    path('game/2/', views.game2, name='game2'),
    path('game/3/', views.game3, name='game3'),
    path('game/4/', views.game4, name='game4'),
    path('account/', views.account, name='account'),
    path('account/detail/', views.detail, name='detail'),
    path('account/info/', views.info, name='info'),
    path('account/detail/', views.detail, name='detail'),
    path('account/outcome/', views.outcome, name='outcome'),
    path('account/bet/', views.bet, name='bet'),
    path('account/notice/', views.notice, name='notice'),
    path('account/contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]