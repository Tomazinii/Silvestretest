from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Agenda_test
from register.models import Medico
from django.contrib.auth.decorators import login_required
from .forms import Agendar_form
# Create your views here.

from django.urls import reverse
from medico.models import PacoteEspecialidade





def agendar_consulta(request):
	consulta = Medico.objects.all()
	pacotes = PacoteEspecialidade.objects.all()



	return render(request, "pages/agendar_consulta.html",{'consulta':consulta,'pacotes':pacotes})

def agendar_consulta_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("anunciar_form"))
    else:
        especialidade=request.POST.get("especialidade")
        tipo_de_consulta=request.POST.get("tipo_de_consulta")
        data_nascimento=request.POST.get("data_nascimento")
        genero=request.POST.get("genero")

        forma_de_pagamento = request.POST.get("forma_de_pagamento")
        horario_agendado=request.POST.get("horario")
        cpf = request.POST.get("cpf")
        nome_completo =request.POST.get("nome")
        email = request.POST.get("email")
        celular =request.POST.get("celular")



        try:
            multistepform=Agenda_test(especialidade=especialidade,tipo_de_consulta=tipo_de_consulta,data_nascimento=data_nascimento,genero=genero,horario_agendado=horario_agendado,cpf=cpf,nome_completo=nome_completo,email=email,celular=celular,forma_de_pagamento=forma_de_pagamento)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('home'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('anunciar_form'))



def agendar_exame(request):
	return render(request, "pages/agendar_exame.html")




