# Generated by Django 2.1.2 on 2018-11-19 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_complaint', '0009_auto_20181116_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accepted',
            name='answer',
            field=models.CharField(choices=[('ECNS', 'ECNS'), ('Tramite', 'Tramite'), ('S', 'S'), ('PS', 'PS'), ('PR', 'PR')], default='S', max_length=100, verbose_name='Actual Respuesta de la queja'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Esperando Respuesta de Tecnico', 'ERT'), ('Esperando Asignacion', 'EA'), ('Esperando aceptacion del jefe', 'EAJ'), ('Pendiente', 'P')], default='Pendiente', max_length=20, verbose_name='Estado de la Queja'),
        ),
    ]
