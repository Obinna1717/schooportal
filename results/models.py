from django.db import models
from django.conf import settings
from courses.models import Course


class Result(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
       Course,
       on_delete=models.CASCADE,
       related_name="results"
    )

    score = models.PositiveIntegerField()

    grade = models.CharField(max_length=2)

    session = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student.email} - {self.course.course_code}"