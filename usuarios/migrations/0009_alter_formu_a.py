# Generated by Django 3.2.8 on 2021-11-23 00:08

from django.conf import settings
import django.contrib.auth.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0008_formu_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formu',
            name='a',
            field=models.ForeignKey(on_delete=django.contrib.auth.forms.UsernameField, to=settings.AUTH_USER_MODEL),
        ),
    ]