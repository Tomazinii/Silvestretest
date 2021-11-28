from django.db.models.signals import post_save, pre_delete
from register.models import Medico
from django.dispatch import receiver
from .models import PacoteEspecialidade

@receiver(post_save, sender=Medico)
def post_save_create_profile(sender, instance, created, **kwargs):

    if created:
        PacoteEspecialidade.objects.create(medico_e_especialidade=instance,nome_especialidade=instance.Especialidade,nome_medico=instance.user.username)