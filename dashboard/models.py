from django.db import models
from accounts.models import Lecturer, Student
from courses.models import Course


class Assignment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    title = models.CharField(max_length=50)

    description = models.TextField()

    due_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Lecturer,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class PostAssignment(models.Model):
    
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    

    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE, related_name='post_assignments')
    
    file = models.FileField(upload_to='assignments/')

    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"{self.lecturer} - {self.title}"   
    


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(PostAssignment,on_delete=models.CASCADE)
    
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE, related_name='assignment_submissions')

    student = models.ForeignKey(Student,on_delete=models.CASCADE)

    file = models.FileField(upload_to='submissions/')

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.assignment}"


class Result(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE, related_name='dashboard_results')

    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    grade = models.CharField(max_length=2)

    score = models.DecimalField(max_digits=5,decimal_places=2)

    session = models.CharField(max_length=50)

    semester = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.student} - {self.course}"
    
class Attendance(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    marked_by = models.ForeignKey(
        Lecturer,
        on_delete=models.CASCADE
    )

    date = models.DateField(auto_now_add=True)

    present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'course', 'date')

    def __str__(self):
        return f"{self.student} - {self.course} ({self.date})"


class Announcement(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    lecturer = models.ForeignKey(
        Lecturer,
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title 
    
    
# class  AssignmentView(models.Model):
#     assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
#     lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
#     viewed_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('assignment', 'lecturer')

#     def __str__(self):
#         return f"{self.lecturer} - {self.assignment}"      