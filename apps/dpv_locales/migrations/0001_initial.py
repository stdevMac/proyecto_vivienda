# Generated by Django 2.1 on 2019-01-23 02:02

import apps.dpv_locales.validators
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
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_created=True, auto_now_add=True, help_text='Fecha en que se introdujo el local al sistema.')),
                ('direccion_numero', models.CharField(help_text='Numero de la dirección', max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]', message='Este campo debe comenzar por un número.')], verbose_name='Número')),
                ('no_viviendas', models.PositiveSmallIntegerField(help_text='Total de viviendas en el local', validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Total de viviendas')),
                ('aprobado', models.BooleanField(default=False, help_text='Marque si está aprobado el local')),
                ('pendiente', models.PositiveSmallIntegerField(help_text='Viviendas pendientes de aprobación', validators=[django.core.validators.MaxValueValidator(50)], verbose_name='Pendientes de aprobación')),
                ('acta', models.CharField(max_length=9, validators=[apps.dpv_locales.validators.validate_acta_acuerdo], verbose_name='Acta')),
                ('acuerdoCAM', models.CharField(blank=True, default='', max_length=9, validators=[apps.dpv_locales.validators.validate_acta_acuerdo], verbose_name='Acuerdo CAM')),
                ('acuerdoPEM', models.CharField(blank=True, default='', max_length=9, validators=[apps.dpv_locales.validators.validate_acta_acuerdo], verbose_name='Acuerdo PEM')),
                ('acuerdoORG', models.CharField(blank=True, default='', max_length=9, validators=[apps.dpv_locales.validators.validate_acta_acuerdo], verbose_name='Acuerdo Organismo')),
                ('observaciones', models.TextField(max_length=600, verbose_name='Otras observaciones')),
                ('estatal', models.BooleanField(default=True, verbose_name='Es estatal')),
                ('acuerdo_DPV', models.CharField(blank=True, default='', max_length=9, validators=[apps.dpv_locales.validators.validate_acta_acuerdo], verbose_name='Acuerdo DPV')),
                ('data_ok', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)])),
                ('system_info', models.TextField(blank=True, default='', max_length=300)),
                ('consejo_popular', models.ForeignKey(blank=True, default=None, help_text='Consejo popular donde se encuetra ubicado el Local', null=True, on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.ConsejoPopular', verbose_name='Consejo Popular')),
                ('direccion_calle', models.ForeignKey(help_text='Calle de la direccion', on_delete=django.db.models.deletion.CASCADE, related_name='calle_principal', to='dpv_nomencladores.Calle', verbose_name='Calle')),
                ('direccion_entre1', models.ForeignKey(help_text='Primera entre calle de la dirección', max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='entrecalle1', to='dpv_nomencladores.Calle', verbose_name='Primera Entrecalle')),
                ('direccion_entre2', models.ForeignKey(help_text='Segunda entre calle de la dirección', max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='entrecalle2', to='dpv_nomencladores.Calle', verbose_name='Segunda Entrecalle')),
                ('municipio', models.ForeignKey(help_text='Municipio donde se encuentra ubicado el local el local', on_delete='Null', related_name='locales_mun', to='dpv_nomencladores.Municipio')),
                ('organismo', models.ForeignKey(help_text='Organismo que ocupa el local', on_delete=django.db.models.deletion.CASCADE, related_name='locales_org', to='dpv_nomencladores.Organismo')),
                ('piso', models.ForeignKey(help_text='Piso de la direccion del local', on_delete=django.db.models.deletion.CASCADE, to='dpv_nomencladores.Piso')),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
                'ordering': ['fecha'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='local',
            unique_together={('municipio', 'direccion_calle', 'direccion_numero', 'piso')},
        ),
    ]
