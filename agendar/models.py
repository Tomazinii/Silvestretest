from django.db import models

# Create your models here.
from register.models import Medico,CustomUser



class Agendar_consulta(models.Model):
    data_da_consulta_marcada = models.DateTimeField(auto_now=False, auto_now_add=False)
    data_criado_agendamento = models.DateTimeField(auto_now=True, auto_now_add=False)
    medico_e_especialidade = models.ForeignKey(Medico,on_delete=models.CASCADE)
    paciente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_payment = models.BooleanField(default=False)



    def __str__(self):
        return f'Agendamento {self.paciente}-{self.medico_e_especialidade.Especialidade}'
    

    class Meta:
        ordering = ['data_da_consulta_marcada',]



class Agenda_test(models.Model): # agenda instance, provisória para usuários que nao possuem conta cadastrada
    especialidade = models.CharField(max_length=50,default='')
    tipo_de_consulta = models.CharField(max_length=50,default='')
    data_nascimento=models.CharField(max_length=12,default='')
    genero = models.CharField(max_length=50)

    horario_agendado=models.CharField(max_length=50,default='')
    forma_de_pagamento = models.CharField(max_length=50,default='')
    cpf = models.CharField(max_length=50,default='')
    nome_completo =models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=254,default='')
    celular = models.CharField(max_length=50,default='')


#data_agendada



