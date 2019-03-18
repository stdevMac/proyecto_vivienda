# Generated by Django 2.1.7 on 2019-03-17 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_complaint', '0011_auto_20190228_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accepted',
            name='answer',
            field=models.CharField(choices=[('ECNS', 'Explicada Causa de no Solucion'), ('PS', 'Pendiente de Solucion'), ('S', 'Solucion o Resuelto'), ('Tramite', 'Tramite'), ('PR', 'Pendiente de Respuesta')], default='S', max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Finalizada', 'F'), ('Pendiente', 'P'), ('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='boss_answer',
            field=models.CharField(choices=[('ECNS', 'Explicada Causa de no Solucion'), ('PS', 'Pendiente de Solucion'), ('S', 'Solucion o Resuelto'), ('Tramite', 'Tramite'), ('PR', 'Pendiente de Respuesta')], default='S', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='current_status',
            field=models.CharField(choices=[('Finalizada', 'F'), ('Pendiente', 'P'), ('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='state',
            field=models.CharField(choices=[('Finalizada', 'F'), ('Pendiente', 'P'), ('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=200),
        ),
    ]
