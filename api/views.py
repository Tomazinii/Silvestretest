from django.shortcuts import render

# Create your views here.
def testview(request):
    if request.session.get('teste') is None:
        request.session['teste'] = 'ok'
    return render(request, "pages/home.html")


from rest_framework import viewsets
from .serializers import TodoSerializer,TestSerializer,MedicoSerializer,PacoteEspecialidadeSerializer
from agendar.models import Agendar_consulta,Agenda_test

from register.models import Medico

from medico.models import PacoteEspecialidade

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Agendar_consulta.objects.all()



class TestView(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Agenda_test.objects.all()


class MedicoView(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()


class PacoteEspecialidadeView(viewsets.ModelViewSet):
    serializer_class = PacoteEspecialidadeSerializer
    queryset = PacoteEspecialidade.objects.all()


