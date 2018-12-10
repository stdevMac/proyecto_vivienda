# Generated by Django 2.1 on 2018-12-09 06:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personajuridica',
            name='movil',
            field=models.CharField(blank=True, max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Movil'),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')]),
        ),
        migrations.AlterField(
            model_name='personajuridica',
            name='telefono',
            field=models.CharField(blank=True, max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Fijo'),
        ),
        migrations.AlterField(
            model_name='personanatural',
            name='apellidos',
            field=models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')]),
        ),
        migrations.AlterField(
            model_name='personanatural',
            name='ci',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11, message='Este campo no puede tener menos de 11 caracteres'), django.core.validators.MaxLengthValidator(11, message='Este campo no puede tener más de 11 caracteres'), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')]),
        ),
        migrations.AlterField(
            model_name='personanatural',
            name='movil',
            field=models.CharField(blank=True, max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Movil'),
        ),
        migrations.AlterField(
            model_name='personanatural',
            name='nombre',
            field=models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')]),
        ),
        migrations.AlterField(
            model_name='personanatural',
            name='telefono',
            field=models.CharField(blank=True, max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Fijo'),
        ),
    ]
