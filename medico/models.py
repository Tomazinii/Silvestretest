from django.db import models
from register.models import Medico

# Create your models here.

"""from register.models import Medico

class Especialidade(models.Model):
    medico = models.ManyToManyField("Medico")
   
    
"""



class PacoteEspecialidade(models.Model):
    medico_e_especialidade = models.ForeignKey(Medico, on_delete=models.CASCADE)
    horario_disponivel = models.CharField(max_length=50)
    disponibilidade = models.BooleanField(default=True)
    nome_medico = models.CharField(max_length=50,default='')
    nome_especialidade = models.CharField(max_length=50,default='')
    

