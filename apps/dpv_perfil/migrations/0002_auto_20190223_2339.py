# Generated by Django 2.1 on 2019-02-23 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
