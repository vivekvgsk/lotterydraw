from django.db import models

# Create your models here.

class Lottery(models.Model):
    lottery_no=models.IntegerField(max_length=7)
    lottery_price=models.IntegerField(max_length=8)


