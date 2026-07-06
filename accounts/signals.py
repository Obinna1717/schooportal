from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User
from .models import Student, Lecturer


@receiver(post_save, sender=User)
def create_role_accounts(sender, instance, created, **kwargs):
    if created:
        print("Signal executed for:", instance.username)
        if instance.role == "student":
            Student.objects.get_or_create(
                user=instance,
                defaults={
                    "matric_number": f"MAT{instance.id:05d}",
                    "full_name": instance.username,
                    "level": 100,
                },
            )

        elif instance.role == "lecturer":
            Lecturer.objects.get_or_create(
                user=instance,
                defaults={
                    "staff_id": f"STF{instance.id:05d}",
                },
            )