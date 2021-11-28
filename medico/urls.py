from django.urls import path

from . import views


urlpatterns = [
    path('medico/<int:pk>',views.portal_medico,name='medico')

]
