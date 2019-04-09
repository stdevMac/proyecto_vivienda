# Generated by Django 2.1 on 2019-03-18 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfigurate',
            name='puerto',
            field=models.PositiveSmallIntegerField(blank=True, help_text='Puerto de conección al servidor.', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Puerto'),
        ),
    ]
