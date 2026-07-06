from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    

    registration_number = models.CharField(max_length=20, unique=True)

    department = models.CharField(max_length=100)

    level = models.PositiveIntegerField()
    
    sex = models.CharField(max_length=10)

    
    def __str__(self):
        return f"{self.user.email} profile"
    
    