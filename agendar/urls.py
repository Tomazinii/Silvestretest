from django.urls import path
from . import views

urlpatterns = [
	path('agendar_consulta/', views.agendar_consulta,name='agendar_consulta'),		 # O certo seria add esse nome de path na url main
	path('agendar_consulta_save/',views.agendar_consulta_save,name='agendar_save'),
	path('agendar-exame/', views.agendar_exame,name='agendar_exame'), # O certo seria add esse nome de path na url main
]
