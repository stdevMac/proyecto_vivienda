# Generated by Django 2.1 on 2018-12-28 22:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Área de Trabajo')),
                ('numero', models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Calle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la calle', max_length=50, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Calle')),
            ],
            options={
                'verbose_name': 'Calle',
                'verbose_name_plural': 'Calles',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='CentroTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la unidad.', max_length=50, unique=True, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Centro de trabajo')),
                ('siglas', models.CharField(help_text='Siglas de la entidad.', max_length=5, validators=[django.core.validators.MaxLengthValidator(5), django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Siglas')),
                ('numero', models.CharField(blank=True, help_text='Número de la unidad', max_length=2, validators=[django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números'), django.core.validators.MaxLengthValidator(2)], verbose_name='Número')),
                ('oc', models.BooleanField(default=False, help_text='Indica si la unidad es la oficina central', verbose_name='Oficina Central')),
            ],
            options={
                'verbose_name': 'Unidad',
                'verbose_name_plural': 'Unidades',
                'ordering': ['numero', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Concepto')),
            ],
            options={
                'verbose_name': 'Concepto',
                'verbose_name_plural': 'Conceptos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Identificador del destino', max_length=50, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Destino')),
            ],
            options={
                'verbose_name': 'Destino',
                'verbose_name_plural': 'Destinos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=9, unique=True, validators=[django.core.validators.MaxLengthValidator(9), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')], verbose_name='Género')),
                ('sigla', models.CharField(max_length=1, unique=True, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(1), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')], verbose_name='Inicial')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del municipio', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Municipio')),
                ('numero', models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'ordering': ['numero'],
            },
        ),
        migrations.CreateModel(
            name='Organismo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del organismo.', max_length=50, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name=' Organismo')),
                ('siglas', models.CharField(help_text='Siglas representativas del organismo', max_length=7, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")])),
            ],
            options={
                'verbose_name': 'Organismo',
                'verbose_name_plural': 'Organismos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Piso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del piso', max_length=2, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Piso')),
            ],
            options={
                'verbose_name': 'Piso',
                'verbose_name_plural': 'Pisos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del municipio', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('[a-zA-Z0-9]', message="Este campos no puede contener caracteres especiales, ejem. '@', '#', '!', '.', '%', ")], verbose_name='Provincia')),
                ('numero', models.CharField(max_length=2, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Número')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'ordering': ['numero'],
            },
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='dpv_nomencladores.Provincia'),
        ),
        migrations.AddField(
            model_name='centrotrabajo',
            name='municipio',
            field=models.ForeignKey(help_text='Municipio donde está ubicado el centro.', on_delete=django.db.models.deletion.CASCADE, related_name='ubicacion_work', to='dpv_nomencladores.Municipio'),
        ),
    ]
