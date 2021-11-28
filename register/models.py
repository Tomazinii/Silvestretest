from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email address'), unique=True)
    REQUIRED_FIELDS = []
    is_medico = models.BooleanField(default=False)
    is_paciente = models.BooleanField(default=False)


class Paciente(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class Medico(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    CRM = models.CharField(max_length=50)
    Especialidade = models.CharField(max_length=50,)

    def __str__(self):
        return f'Dr. {self.user.username}'
    
