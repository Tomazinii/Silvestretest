from django.shortcuts import render,redirect

from django.http.response import HttpResponseNotFound

from register.models import CustomUser
# Create your views here.

def portal_medico(request,pk):
	user = CustomUser.objects.get(pk=pk)
	if request.user.is_medico and request.user.pk==pk:
		return render(request, "pages/portal_medico.html")
	else:
		return HttpResponseNotFound()