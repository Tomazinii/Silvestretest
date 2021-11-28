from django.urls import path

from .views import portal_paciente

urlpatterns = [
    path('paciente/<int:pk>',portal_paciente,name='paciente')
]
