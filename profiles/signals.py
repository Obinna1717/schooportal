from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import Lecturer, User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(
            user=instance,
            defaults={
                "registration_number": f"REG{instance.id:05d}",
                "department": "N/A",
                "level": 100,
                "sex": "N/A",
            }
        )
        
        
    elif instance.role == "lecturer":
            Lecturer.objects.get_or_create(
                user=instance,
                defaults={
                    "staff_id": f"STF{instance.id:05d}",
                },
            )    