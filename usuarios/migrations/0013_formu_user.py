# Generated by Django 3.2.8 on 2021-11-23 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0012_remove_formu_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='formu',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.user'),
            preserve_default=False,
        ),
    ]