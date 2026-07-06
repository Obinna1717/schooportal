from django.db import models
from django.conf import settings


class SchoolFee(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    reference = models.CharField(max_length=100, unique=True)

    paid_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20, default='Paid')

    def __str__(self):
        return f"{self.student.email} - {self.reference}"