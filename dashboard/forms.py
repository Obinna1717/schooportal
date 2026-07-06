from django import forms
from courses.models import Course, CourseMaterial
from .models import AssignmentSubmission, PostAssignment

from django import forms
from .models import Attendance, Announcement


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            "course",
            "student",
            "present"
        ]


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = [
            "course",
            "title",
            "message"
        ]


class CourseMaterialForm(forms.ModelForm):
    class Meta:
        model = CourseMaterial
        fields = [
            "course",
            "title",
            "file"
        ]


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ["file"]
        
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = PostAssignment
        fields = [
            "course",
            "title",
            "lecturer",
            "file",
        ]        


class AttendanceCourseForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        label="Select Course"
    ) 