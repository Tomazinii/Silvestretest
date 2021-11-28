# Generated by Django 3.2.8 on 2021-11-28 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacoteEspecialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario_disponivel', models.CharField(max_length=50)),
                ('disponibilidade', models.BooleanField(default=True)),
                ('nome_medico', models.CharField(default='', max_length=50)),
                ('nome_especialidade', models.CharField(default='', max_length=50)),
                ('medico_e_especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.medico')),
            ],
        ),
    ]