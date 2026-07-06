from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Course, Registration, CourseMaterial

admin.site.register(Course)
admin.site.register(Registration)
admin.site.register(CourseMaterial)
