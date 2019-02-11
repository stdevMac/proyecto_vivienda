# Generated by Django 2.1.2 on 2018-12-14 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_complaint', '0005_auto_20181214_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accepted',
            name='answer',
            field=models.CharField(choices=[('Tramite', 'Tramite'), ('S', 'Solucion o Resuelto'), ('PR', 'Pendiente de Respuesta'), ('ECNS', 'Explicada Causa de no Solucion'), ('PS', 'Pendiente de Solucion')], default='S', max_length=100),
        ),
        migrations.AlterField(
            model_name='accepted',
            name='final_args',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='accepted',
            name='technical_args',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Pendiente', 'P'), ('Finalizada', 'F'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='finishedcomplaint',
            name='technical_args',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='boss_answer',
            field=models.CharField(choices=[('Tramite', 'Tramite'), ('S', 'Solucion o Resuelto'), ('PR', 'Pendiente de Respuesta'), ('ECNS', 'Explicada Causa de no Solucion'), ('PS', 'Pendiente de Solucion')], default='S', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='boss_args',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='current_status',
            field=models.CharField(choices=[('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Pendiente', 'P'), ('Finalizada', 'F'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='state',
            field=models.CharField(choices=[('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Pendiente', 'P'), ('Finalizada', 'F'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=200),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='technical_args',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Documents',
        ),
    ]
