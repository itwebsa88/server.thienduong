from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

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

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    status = models.IntegerField(null=True)
    money = models.DecimalField(max_digits=20, decimal_places=2)
    amount_code = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    paypassword = models.CharField(max_length=100)
    header_img = models.CharField(max_length=50)
    uid = models.IntegerField()
    ip = models.CharField(max_length=50)
    last_time = models.DateTimeField(auto_now_add=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.IntegerField()
    num = models.IntegerField()
    min = models.IntegerField()
    max = models.IntegerField()
    is_online = models.IntegerField()
    role = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    daili = models.CharField(max_length=30)

    @property
    def swapstatus(self):
        if self.status == 1:
            self.status = 0
        else: 
            self.status = 1
        
    def __str__(self):
        return self.username
    
    class Meta:
        managed = False
        db_table = "adminapp_member"

STATUS_TAB = ((1, "SCHEDULED"),
              (2, "FINISHED"),
              (3, "PLAYING")
              )

BET_CHOICES = ((1, 1),
               (2, 2),
               (0, 0)
               )



# class AppUser(models.Model):
#     # TODO: change cash to decimal
#     cash = models.DecimalField(validators=[MinValueValidator(0.00)],
#                                max_digits=6, decimal_places=2)
#     bank_account_number = models.CharField(max_length=64)
#     user = models.OneToOneField(User, on_delete=models.CASCADE,)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Bet(models.Model):
#
#     BET_RESULTS = ((0, "LOST"),
#                    (1, "WON"),
#                    (2, "PENDING")
#                    )
#
#     bet_user = models.ForeignKey(AppUser, related_name="bet_user", on_delete=models.CASCADE,)
#     bet_amount = models.DecimalField(validators=[MinValueValidator(0.01)],
#                                      max_digits=6, decimal_places=2)
#     fixture = models.ForeignKey(Ticket, related_name="fixture", on_delete=models.CASCADE,)
#     bet = models.IntegerField(choices=BET_CHOICES)
#     bet_course = models.FloatField(default=0)
#     # bet result 0: LOST, 1: WIN
#     bet_result = models.IntegerField(default=2, blank=True, choices=BET_RESULTS)