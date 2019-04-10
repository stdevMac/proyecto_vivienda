# Generated by Django 2.1 on 2019-04-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_complaint', '0002_auto_20190410_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accepted',
            name='answer',
            field=models.CharField(choices=[('Trámite', 'Trámite'), ('ECNS', 'Explicada Causa de no Solución'), ('S', 'Solución o Resuelto'), ('PR', 'Pendiente de Respuesta'), ('PS', 'Pendiente de Solución')], default='S', max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Finalizada', 'F'), ('Esperando Respuesta de Técnico', 'ERT'), ('Pendiente', 'P'), ('Esperando aceptación del jefe', 'EAJ'), ('Esperando Asignación', 'EA')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='currentcomplaint',
            name='current_status',
            field=models.CharField(choices=[('Finalizada', 'Finalizada'), ('Esperando Asignación', 'Esperando Asignación'), ('Esperando aceptación del jefe', 'Esperando aceptación del jefe'), ('Esperando Respuesta de Técnico', 'Esperando Respuesta de Técnico'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=100),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='boss_answer',
            field=models.CharField(blank=True, choices=[('Trámite', 'Trámite'), ('ECNS', 'Explicada Causa de no Solución'), ('S', 'Solución o Resuelto'), ('PR', 'Pendiente de Respuesta'), ('PS', 'Pendiente de Solución')], default='S', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='current_status',
            field=models.CharField(choices=[('Finalizada', 'Finalizada'), ('Esperando Asignación', 'Esperando Asignación'), ('Esperando aceptación del jefe', 'Esperando aceptación del jefe'), ('Esperando Respuesta de Técnico', 'Esperando Respuesta de Técnico'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=200),
        ),
    ]
