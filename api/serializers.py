from rest_framework import serializers
from agendar.models import Agendar_consulta,Agenda_test

from register.models import Medico
from medico.models import PacoteEspecialidade


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendar_consulta
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda_test
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'




class PacoteEspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacoteEspecialidade
        fields = '__all__'