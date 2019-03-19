# Generated by Django 2.1.7 on 2019-03-19 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dpv_nomencladores', '0001_initial'),
        ('dpv_locales', '0001_initial'),
        ('dpv_persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveSmallIntegerField()),
                ('cantidad_persona', models.PositiveSmallIntegerField(help_text='Cantidad de personas que viven en la vivienda')),
                ('fecha_propietario', models.DateField(verbose_name='Fecha de habitado')),
                ('aprobada', models.BooleanField(default=False, help_text='Marcar si la vivienda esta aprobada.', verbose_name='Aprobación dada')),
                ('add_concepto', models.CharField(blank=True, max_length=20, verbose_name='Datos Concepto')),
                ('concepto', models.ForeignKey(help_text='Concepto de uso de la vivienda', on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Concepto', verbose_name='Concepto')),
                ('destino', models.ForeignKey(help_text='Destino para la vivienda', on_delete=django.db.models.deletion.CASCADE, related_name='locales_dest', to='dpv_nomencladores.Destino')),
                ('local_dado', models.ForeignKey(default='', help_text='Local donde se encuentra la vivienda.', on_delete=django.db.models.deletion.CASCADE, related_name='vivienda_local', to='dpv_locales.Local')),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vivienada_prop', to='dpv_persona.PersonaNatural')),
            ],
            options={
                'verbose_name': 'Vivienda',
                'verbose_name_plural': 'Viviendas',
                'ordering': ['numero'],
            },
        ),
    ]
