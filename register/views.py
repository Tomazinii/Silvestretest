from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from register.models import CustomUser

from .forms import CreateUserForm,CreateMedicoForm
# Create your views here.


def login_page_paciente(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
        if user is not None and user.is_paciente:
            login(request,user)
            l=request.user.id
            k = request.build_absolute_uri('/')
            return redirect(f'{k}paciente/{l}')  # 
            
        
        else:
            messages.info(request, "Nome ou senha de usuário incorretos! ")
    context = {}
    return render(request,'register/login.html',context)



def login_page_medico(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email,password=password)
        if user is not None and user.is_medico:
            login(request,user)
            l=request.user.id
            k = request.build_absolute_uri('/')
            return redirect(f'{k}medico/{l}')  # 
            
        
        else:
            messages.info(request, "Nome ou senha de usuário incorretos! ")
    context = {}
    return render(request,'register/login_medico.html',context)


def logout_page(request):
    logout(request)
    return redirect('login')
    

def logout_page_medico(request):
    logout(request)
    return redirect('login_medico')
    

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register/signup.html', context)



class MedicoRegister(CreateView):
    model = CustomUser
    form_class = CreateMedicoForm
    template_name = 'register/signup_medico.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'medico'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('login_medico')