# Generated by Django 2.1 on 2019-03-15 14:27

import apps.dpv_perfil.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_perfil', '0002_auto_20190223_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=apps.dpv_perfil.models.scramble_upload_avatar, verbose_name='avatars'),
        ),
    ]
