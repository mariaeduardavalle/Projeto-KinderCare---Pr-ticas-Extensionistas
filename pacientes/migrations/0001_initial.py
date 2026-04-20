from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('terapeutas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('responsavel', models.CharField(max_length=150)),
                ('contato', models.CharField(max_length=20)),
                ('observacoes', models.TextField(blank=True)),
                ('terapeutas_responsaveis', models.ManyToManyField(blank=True, related_name='pacientes', to='terapeutas.terapeuta')),
            ],
        ),
        migrations.CreateModel(
            name='TerapiaPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_terapia', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='terapias', to='pacientes.paciente')),
            ],
        ),
    ]
