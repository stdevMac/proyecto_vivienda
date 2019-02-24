# Generated by Django 2.1 on 2019-01-23 02:02

import apps.dpv_persona.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dpv_nomencladores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaJuridica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30)])),
                ('direccion_numero', models.PositiveSmallIntegerField(blank=True, verbose_name='Número')),
                ('telefono', models.CharField(blank=True, max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Fijo')),
                ('movil', models.CharField(blank=True, max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Movil')),
                ('email_address', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('sigla', models.CharField(blank=True, help_text='Siglas identificativas de la entidad.', max_length=10, verbose_name='Siglas')),
                ('nombre_contacto', models.CharField(blank=True, help_text='Nombre que se usara para el contacto con la entidad.', max_length=200, verbose_name='Nombre de contacto')),
                ('codigo_nit', models.CharField(help_text='Código NiT de la entidad', max_length=11, verbose_name='Código NiT')),
                ('codigo_reuup', models.CharField(help_text='Código Reeup de la Entidad', max_length=11, verbose_name='Código Reeup')),
                ('direccion_calle', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Calle', verbose_name='Calle')),
                ('direccion_entrecalle1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personaj_entrecalle1', to='dpv_nomencladores.Calle', verbose_name='Primera Entrecalle')),
                ('direccion_entrecalle2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='personaj_entrecalle2', to='dpv_nomencladores.Calle', verbose_name='Segunda Entrecalle')),
                ('municipio', models.ForeignKey(help_text='Municipio donde recide la persona', on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Persona Jurídica',
                'verbose_name_plural': 'Personas Jurídicas',
            },
        ),
        migrations.CreateModel(
            name='PersonaNatural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_numero', models.PositiveSmallIntegerField(blank=True, verbose_name='Número')),
                ('telefono', models.CharField(blank=True, max_length=8, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Fijo')),
                ('movil', models.CharField(blank=True, max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números')], verbose_name='Teléfono Movil')),
                ('email_address', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('nombre', models.CharField(max_length=30, validators=[django.core.validators.MaxLengthValidator(30), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')])),
                ('apellidos', models.CharField(max_length=50, validators=[django.core.validators.MaxLengthValidator(50), django.core.validators.RegexValidator('^[a-zA-Z ]*[a-zA-Z ]$', message='Este campo solo puede contener letras')])),
                ('ci', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11, message='Este campo no puede tener menos de 11 caracteres'), django.core.validators.MaxLengthValidator(11, message='Este campo no puede tener más de 11 caracteres'), django.core.validators.RegexValidator('^[0-9]*[0-9]$', message='Este campo solo puede contener números'), apps.dpv_persona.validators.ci_validate], verbose_name='CI')),
                ('direccion_calle', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Calle', verbose_name='Calle')),
                ('direccion_entrecalle1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='persona_entrecalle1', to='dpv_nomencladores.Calle', verbose_name='Primera Entrecalle')),
                ('direccion_entrecalle2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='persona_entrecalle2', to='dpv_nomencladores.Calle', verbose_name='Segunda Entrecalle')),
                ('genero', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Genero', verbose_name='Género')),
                ('municipio', models.ForeignKey(help_text='Municipio donde recide la persona', on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Municipio', verbose_name='Municipio')),
            ],
            options={
                'verbose_name': 'Persona Natural',
                'verbose_name_plural': 'Personas Naturales',
                'ordering': ['ci', 'apellidos'],
            },
        ),
    ]
