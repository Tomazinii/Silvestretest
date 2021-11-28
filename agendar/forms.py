from django.forms import ModelForm,widgets
from .models import Agenda_test
from django import forms

from .models import Agendar_consulta


class Agendar_form(ModelForm):
	
		class Meta:
			model = Agenda_test
			fields ='__all__'


			CHOICES = (
				('genero', 'Sexo'),
				('maculino', 'Masculino'),
				('feminino', 'Feminino'),
			)
			CHOICES_TIPO = (
				('Presencial', 'Presencial'),
				('Teleconsulta', 'Teleconsulta'),

			)
			widgets = {
            'especialidade':forms.Select(choices=CHOICES,attrs={'class':'select-especialidade'}),
			'tipo_de_consulta':forms.RadioSelect(attrs={'class':'checkbox'},choices=CHOICES_TIPO ),
			'data_nascimento':forms.TextInput(attrs={'id':"datay", "placeholder":"dd/mm/aa"}),
			'genero':forms.Select(choices=CHOICES,attrs={'class':'select-genero'}),

            }
