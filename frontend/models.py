from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=20)
    ip = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    bankAccount = models.CharField(max_length=30)
    bankName = models.CharField(max_length=30)
    birthday = models.DateField()
    createAt = models.DateField(auto_created=True)
    status = models.IntegerField()
    staffId = models.CharField(max_length=20)
    activeAt = models.DateField(auto_now=True)
class BetList(models.Model):
    betId = models.CharField(max_length=20)
    betPharseID = models.CharField(max_length=20)
    betVal = models.IntegerField()
    betChoice = models.CharField(max_length=20)
    userName = models.CharField(max_length=20)
    createAt = models.DateField(auto_now=True)
class BetPharse(models.Model):
    betPharseID = models.CharField(max_length=20)
    betResult = models.CharField(max_length=20)
class Balance(models.Model):
    userName = models.CharField(max_length=20)
    balance = models.IntegerField()
class Bank(models.Model):
    userName = models.CharField(max_length=20)
    type = models.IntegerField()
    value = models.IntegerField()