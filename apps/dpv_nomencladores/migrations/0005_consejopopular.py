# Generated by Django 2.1 on 2018-12-26 13:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_nomencladores', '0004_auto_20181214_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsejoPopular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del consejo popular', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Consejo Popular')),
                ('numero', models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator('[0-9]', message='Este campo solo puede contener números')], verbose_name='Número')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='dpv_nomencladores.Municipio')),
            ],
            options={
                'verbose_name': 'Consejo Popular',
                'verbose_name_plural': 'Consejos Populares',
                'ordering': ['numero'],
            },
        ),
    ]
