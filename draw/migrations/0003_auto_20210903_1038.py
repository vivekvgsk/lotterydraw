# Generated by Django 3.2.3 on 2021-09-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0002_alter_lottery_lottery_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='lottery_no',
            field=models.CharField(max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='lottery',
            name='lottery_price',
            field=models.IntegerField(),
        ),
    ]