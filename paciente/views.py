from django.shortcuts import render
from register.models import CustomUser,Paciente
from agendar.models import Agendar_consulta
from django.http.response import HttpResponseNotFound
import calendar
from django.contrib import messages
# Create your views here.
def portal_paciente(request,pk):
    user = CustomUser.objects.get(pk=pk)
    if user.is_paciente and request.user.pk==pk:

        try:
            if Agendar_consulta.objects.filter(paciente=request.user):
                consulta = Agendar_consulta.objects.filter(paciente=request.user)
                return render(request, "pages/portal_paciente.html",{'consulta':consulta})
        except:
                messages.info(request, 'Você não possui nenhum agendamento')
                return render(request, "pages/portal_paciente.html")
    else:
        return HttpResponseNotFound()