from django.db import models

# Create your models here.

class Lottery(models.Model):
    lottery_no=models.CharField(max_length=7,unique=True)
    lottery_price=models.IntegerField()

    def __str__(self):
        return self.lottery_no


