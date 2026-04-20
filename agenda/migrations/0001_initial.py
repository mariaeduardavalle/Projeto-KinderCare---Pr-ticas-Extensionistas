from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('pacientes', '0001_initial'),
        ('terapeutas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendaSemanal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_terapia', models.CharField(max_length=100)),
                ('dia_semana', models.IntegerField(choices=[(0, 'Segunda-feira'), (1, 'Terça-feira'), (2, 'Quarta-feira'), (3, 'Quinta-feira'), (4, 'Sexta-feira')])),
                ('horario', models.TimeField()),
                ('ativo', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamentos', to='pacientes.paciente')),
                ('terapeuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamentos', to='terapeutas.terapeuta')),
            ],
            options={'verbose_name': 'Agenda semanal', 'verbose_name_plural': 'Agenda semanal', 'ordering': ['dia_semana', 'horario']},
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_terapia', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('tipo', models.CharField(choices=[('normal', 'Normal'), ('extra', 'Extra')], default='normal', max_length=10)),
                ('status_presenca', models.CharField(choices=[('agendado', 'Agendado'), ('presente', 'Presente'), ('falta', 'Falta'), ('falta_justificada', 'Falta justificada')], default='agendado', max_length=20)),
                ('observacao_presenca', models.CharField(blank=True, max_length=255)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('agenda_semanal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='atendimentos', to='agenda.agendasemanal')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendimentos', to='pacientes.paciente')),
                ('terapeuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendimentos', to='terapeutas.terapeuta')),
            ],
            options={'ordering': ['data', 'horario'], 'unique_together': {('paciente', 'terapeuta', 'data', 'horario', 'tipo')}},
        ),
    ]
