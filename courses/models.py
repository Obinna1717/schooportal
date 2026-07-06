from django.db import models

from accounts.models import Department, Lecturer, Student


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    
    course_title = models.CharField(max_length=200)
    
    units = models.PositiveIntegerField()
    
    semester = models.CharField(max_length=15)

    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_code


class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)

    session = models.CharField(max_length=50)

    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course', 'session')

    def __str__(self):
        return f"{self.student.full_name} - {self.course.course_code}"


class CourseMaterial(models.Model): 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    uploaded_by = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='materials/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title