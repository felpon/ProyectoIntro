# Generated by Django 3.2.8 on 2021-11-30 23:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_formu_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='formu',
            name='puntaje',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formu',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 30, 23, 46, 46, 751109, tzinfo=utc), null=True),
        ),
    ]