# Generated by Django 3.2.8 on 2021-11-11 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20211111_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='username',
            new_name='name',
        ),
    ]
