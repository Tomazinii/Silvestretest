from django.contrib import admin


from .models import CustomUser,Medico,Paciente
# Register your models here.

@admin.register(CustomUser)
class OderRegister(admin.ModelAdmin):
    list_display = ['username','email','id']

admin.site.register(Medico)

admin.site.register(Paciente)