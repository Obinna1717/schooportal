from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ("student", "Student"),
        ("lecturer", "Lecturer"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return self.email


class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    matric_number = models.CharField(max_length=50, unique=True)

    full_name = models.CharField(max_length=100)

    level = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Lecturer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    staff_id = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=70, unique=True)

    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
        
   