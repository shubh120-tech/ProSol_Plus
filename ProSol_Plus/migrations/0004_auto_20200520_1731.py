# Generated by Django 3.0.5 on 2020-05-20 12:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProSol_Plus', '0003_userfile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfile',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 17, 31, 50, 646696)),
        ),
    ]
