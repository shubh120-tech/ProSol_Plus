# Generated by Django 3.0.5 on 2020-05-20 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProSol_Plus', '0008_auto_20200520_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 18, 38, 7, 578981)),
        ),
    ]
