# Generated by Django 2.1.7 on 2019-04-02 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpv_complaint', '0002_auto_20190323_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('Esperando Respuesta de Técnico', 'Esperando Respuesta de Técnico'), ('Esperando Asignación', 'Esperando Asignación'), ('Finalizada', 'Finalizada'), ('Esperando aceptación del jefe', 'Esperando aceptación del jefe'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='accepted',
            name='answer',
            field=models.CharField(choices=[('Trámite', 'Trámite'), ('S', 'Solución o Resuelto'), ('PR', 'Pendiente de Respuesta'), ('PS', 'Pendiente de Solución'), ('ECNS', 'Explicada Causa de no Solución')], default='S', max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.CharField(choices=[('Pendiente', 'P'), ('Esperando Respuesta de Técnico', 'ERT'), ('Esperando aceptación del jefe', 'EAJ'), ('Finalizada', 'F'), ('Esperando Asignación', 'EA')], default='Pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='boss_answer',
            field=models.CharField(blank=True, choices=[('Trámite', 'Trámite'), ('S', 'Solución o Resuelto'), ('PR', 'Pendiente de Respuesta'), ('PS', 'Pendiente de Solución'), ('ECNS', 'Explicada Causa de no Solución')], default='S', max_length=20),
        ),
        migrations.AlterField(
            model_name='historycomplaint',
            name='current_status',
            field=models.CharField(choices=[('Esperando Respuesta de Técnico', 'Esperando Respuesta de Técnico'), ('Esperando Asignación', 'Esperando Asignación'), ('Finalizada', 'Finalizada'), ('Esperando aceptación del jefe', 'Esperando aceptación del jefe'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=200),
        ),
        migrations.AddField(
            model_name='currentcomplaint',
            name='complaint',
            field=models.ForeignKey(on_delete=False, to='dpv_complaint.Complaint'),
        ),
    ]
