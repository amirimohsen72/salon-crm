from django.db.models.signals import post_save
from django.dispatch import receiver
from appointments.models import Appointment


@receiver(post_save, sender=Appointment)
def appointment_saved_signal(sender, instance, created, **kwargs):
    if created:
        print(f"[SIGNAL] Appointment created: {instance}")
    else:
        print(f"[SIGNAL] Appointment updated: {instance}")