from django.urls import path
from django.contrib.auth import views as auth_views

from . import views





urlpatterns = [
    path('login/',views.login_page_paciente, name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('logout_medico/',views.logout_page_medico,name='logout_medico'),
    path('register/', views.registerPage, name="register"),
    path('register_medico/',views.MedicoRegister.as_view(),name='register_medico'),
    path('medico/',views.login_page_medico,name='login_medico'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(), 
        name="password_reset_complete"),
    
]
