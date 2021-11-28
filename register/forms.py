
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Medico,Paciente
from django import forms

from django.db import transaction


class CreateUserForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser



    @transaction.atomic

    def save(self):
        user = super().save(commit= False)
        user.email=self.cleaned_data.get('email')
        user.is_paciente = True
        user.save()
        paciente = Paciente.objects.create(user=user)
        paciente.save()
        return paciente


class CreateMedicoForm(UserCreationForm):
    email=forms.EmailField(required=True)
    especialidade=forms.CharField(required=True)
    CRM=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser


    @transaction.atomic

    def save(self):
        user = super().save(commit= False)
        user.email=self.cleaned_data.get('email')
        user.is_medico = True
        user.save()
        medico = Medico.objects.create(user=user)
        medico.Especialidade =self.cleaned_data.get('especialidade')
        medico.CRM=self.cleaned_data.get('CRM')
        medico.save()
        return medico

    