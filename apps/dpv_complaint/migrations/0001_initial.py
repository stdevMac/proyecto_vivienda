# Generated by Django 2.1.2 on 2018-12-07 23:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dpv_perfil', '0001_initial'),
        ('dpv_nomencladores', '0001_initial'),
        ('dpv_persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accepted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('answer', models.CharField(choices=[('Tramite', 'Tramite'), ('PR', 'Pendiente de Respuesta'), ('PS', 'Pendiente de Solucion'), ('S', 'Solucion o Resuelto'), ('ECNS', 'Explicada Causa de no Solucion')], default='S', max_length=100)),
                ('boss_accepted', models.ForeignKey(default=False, on_delete=False, related_name='boss_accepted', to='dpv_perfil.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedToTechnician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=50)),
                ('body', models.CharField(max_length=1000)),
                ('topic', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=15)),
                ('status', models.CharField(choices=[('Pendiente', 'P'), ('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=20)),
                ('enter_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_natural', models.BooleanField(default=True)),
                ('department', models.ForeignKey(null=True, on_delete=False, related_name='department', to='dpv_nomencladores.AreaTrabajo')),
                ('person_juridic', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_juridic', to='dpv_persona.PersonaJuridica')),
                ('person_natural', models.ForeignKey(blank=True, on_delete=False, related_name='person_natural', to='dpv_persona.PersonaNatural')),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FinishedComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('complaint', models.ForeignKey(on_delete=False, to='dpv_complaint.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryComplaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('Pendiente', 'P'), ('Esperando aceptacion del jefe', 'EAJ'), ('Esperando Asignacion', 'EA'), ('Esperando Respuesta de Tecnico', 'ERT')], default='Pendiente', max_length=200)),
                ('boss_answer', models.CharField(choices=[('Tramite', 'Tramite'), ('PR', 'Pendiente de Respuesta'), ('PS', 'Pendiente de Solucion'), ('S', 'Solucion o Resuelto'), ('ECNS', 'Explicada Causa de no Solucion')], default='S', max_length=20)),
                ('date_of_status', models.DateTimeField(auto_now_add=True)),
                ('boss', models.ForeignKey(blank=True, on_delete=False, to='dpv_perfil.Perfil')),
                ('boss_args', models.ForeignKey(blank=True, on_delete=False, related_name='boss_args_history', to='dpv_complaint.Documents')),
                ('complaint', models.ForeignKey(on_delete=False, to='dpv_complaint.Complaint')),
            ],
        ),
        migrations.CreateModel(
            name='Technical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=False, related_name='profile', to='dpv_perfil.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='WaitingForDistribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('complaint', models.ForeignKey(on_delete=False, to='dpv_complaint.Complaint')),
            ],
        ),
        migrations.AddField(
            model_name='historycomplaint',
            name='technical',
            field=models.ForeignKey(blank=True, on_delete=False, related_name='technical_history', to='dpv_complaint.Technical'),
        ),
        migrations.AddField(
            model_name='historycomplaint',
            name='technical_args',
            field=models.ForeignKey(blank=True, on_delete=False, related_name='technical_args_history', to='dpv_complaint.Documents'),
        ),
        migrations.AddField(
            model_name='finishedcomplaint',
            name='technical',
            field=models.ForeignKey(on_delete=False, to='dpv_complaint.Technical'),
        ),
        migrations.AddField(
            model_name='finishedcomplaint',
            name='technical_args',
            field=models.ForeignKey(on_delete=False, related_name='technical_args', to='dpv_complaint.Documents'),
        ),
        migrations.AddField(
            model_name='assignedtotechnician',
            name='complaint',
            field=models.ForeignKey(on_delete=False, to='dpv_complaint.Complaint'),
        ),
        migrations.AddField(
            model_name='assignedtotechnician',
            name='technical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dpv_complaint.Technical'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='complaint',
            field=models.ForeignKey(on_delete=False, to='dpv_complaint.Complaint'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='final_args',
            field=models.ForeignKey(on_delete=False, to='dpv_complaint.Documents'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='technical_args',
            field=models.ForeignKey(on_delete=False, related_name='technical_args_accepted', to='dpv_complaint.Documents'),
        ),
        migrations.AddField(
            model_name='accepted',
            name='technical_work_in_complaint',
            field=models.ForeignKey(default=1, on_delete=False, related_name='technical_accepted', to='dpv_complaint.Technical'),
        ),
    ]
