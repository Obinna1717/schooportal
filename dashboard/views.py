from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DeleteView,
    FormView,
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    View
)

from courses.models import Course, Registration, CourseMaterial
from payments.models import SchoolFee
from results.models import Result
from .models import Announcement, Assignment, AssignmentSubmission, Attendance, PostAssignment
from .forms import AnnouncementForm, AssignmentForm, AttendanceCourseForm, AttendanceForm, CourseMaterialForm, SubmissionForm
from .models import AssignmentSubmission
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView
from django.db.models import Count, Q
from collections import defaultdict
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/student_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print("ROLE:", self.request.user.role)
        print("MATERIALS:", CourseMaterial.objects.count())

        if self.request.user.role == "student":
            student = self.request.user.student

            context["total_courses"] = Registration.objects.filter(student=student).count()
            context["total_payments"] = SchoolFee.objects.filter(student=student).count()
            context["total_results"] = Result.objects.filter(student=student).count()

            courses = Registration.objects.filter(student=student).values_list("course", flat=True)

            context["materials"] = CourseMaterial.objects.all()

            context["submissions"] = AssignmentSubmission.objects.filter(student=student)

        return context


class LecturerDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/lecturer_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.role == "lecturer":
            context["materials"] = CourseMaterial.objects.filter(
                uploaded_by=self.request.user.lecturer
            )

        return context


class UploadMaterialView(LoginRequiredMixin, CreateView):
    model = CourseMaterial
    form_class = CourseMaterialForm
    template_name = "dashboard/upload_material.html"
    success_url = reverse_lazy("lecturer_dashboard")

    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user.lecturer
        return super().form_valid(form)
    
class EditMaterialView(LoginRequiredMixin, UpdateView):
    model = CourseMaterial
    form_class = CourseMaterialForm
    template_name = "dashboard/edit_material.html"
    success_url = reverse_lazy("lecturer_dashboard")

    def get_queryset(self):
        # Lecturer can only edit their own materials
        return CourseMaterial.objects.filter(
            uploaded_by=self.request.user.lecturer
        )


class DeleteMaterialView(LoginRequiredMixin, DeleteView):
    model = CourseMaterial
    template_name = "dashboard/delete_material.html"
    success_url = reverse_lazy("lecturer_dashboard")

    def get_queryset(self):
        # Lecturer can only delete their own materials
        return CourseMaterial.objects.filter(
            uploaded_by=self.request.user.lecturer
        )    
    
    
    
class PostAssignmentView(LoginRequiredMixin, CreateView):
    model = PostAssignment
    form_class = AssignmentForm
    template_name = "dashboard/post_assignment.html"
    success_url = reverse_lazy("lecturer_dashboard")
    
    def form_valid(self, form):
        form.instance.lecturer = self.request.user.lecturer
        return super().form_valid(form)    


class SubmitAssignmentView(LoginRequiredMixin, CreateView):
    model = AssignmentSubmission
    form_class = SubmissionForm
    template_name = "dashboard/submit_assignment.html"
    success_url = reverse_lazy("student_dashboard")

    def form_valid(self, form):
        assignment = get_object_or_404(
            PostAssignment,
            pk=self.kwargs["pk"]
        )

        form.instance.assignment = assignment
        form.instance.course = assignment.course
        form.instance.lecturer = assignment.lecturer
        form.instance.student = self.request.user.student

        return super().form_valid(form)

    
class ViewSubmissionsView(LoginRequiredMixin, ListView):
    model = AssignmentSubmission
    template_name = "dashboard/view_submissions.html"
    context_object_name = "submissions"

    def get_queryset(self):
        if self.request.user.role == "lecturer":
            return AssignmentSubmission.objects.filter(
                lecturer=self.request.user.lecturer
            )

        return AssignmentSubmission.objects.none()  
    
class ViewPostAnnouncementView(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = "dashboard/view_announcements.html"
    context_object_name = "announcements"

    def get_queryset(self):
        if self.request.user.role == "lecturer":
            return Announcement.objects.filter(
                lecturer=self.request.user.lecturer
            )

        return Announcement.objects.none()        


class MarkAttendanceView(LoginRequiredMixin, CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "dashboard/mark_attendance.html"
    success_url = reverse_lazy("lecturer_dashboard")

    def form_valid(self, form):
        form.instance.marked_by = self.request.user.lecturer
        return super().form_valid(form)

class PostAnnouncementView(LoginRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = "dashboard/post_announcement.html"
    success_url = reverse_lazy("lecturer_dashboard")

    def form_valid(self, form):
        form.instance.lecturer = self.request.user
        return super().form_valid(form)  
    
    

class StudentAssignmentListView(LoginRequiredMixin, ListView):
    model = PostAssignment
    template_name = "dashboard/student_assignments.html"
    context_object_name = "assignments"

    def get_queryset(self):
        student = self.request.user.student

        registered_courses = Registration.objects.filter(
            student=student
        ).values_list("course", flat=True)

        return PostAssignment.objects.filter(
            course__in=registered_courses
        ).order_by("-created_at")
        
class EditSubmissionView(LoginRequiredMixin, UpdateView):
    model = AssignmentSubmission
    form_class = SubmissionForm
    template_name = "dashboard/edit_submission.html"
    success_url = reverse_lazy("student_dashboard")

    def get_queryset(self):
        return AssignmentSubmission.objects.filter(
            student=self.request.user.student
        )
        
class DeleteSubmissionView(LoginRequiredMixin, DeleteView):
    model = AssignmentSubmission
    template_name = "dashboard/delete_submission.html"
    success_url = reverse_lazy("student_dashboard")

    def get_queryset(self):
        return AssignmentSubmission.objects.filter(
            student=self.request.user.student
        )
        
class MySubmittedAssignmentsView(LoginRequiredMixin, ListView):
    model = AssignmentSubmission
    template_name = "dashboard/my_submitted_assignment.html"
    context_object_name = "submissions"

    def get_queryset(self):
        return AssignmentSubmission.objects.filter(
            student=self.request.user.student
        ).order_by("-submitted_at")                            
        
class SelectAttendanceCourseView(LoginRequiredMixin, FormView):
    template_name = "dashboard/select_attendance_course.html"
    form_class = AttendanceCourseForm

    def form_valid(self, form):
        course = form.cleaned_data["course"]
        return redirect("take_attendance", pk=course.pk)
    
class TakeAttendanceView(LoginRequiredMixin, View):

    template_name = "dashboard/take_attendance.html"

    def get(self, request, pk):

        course = get_object_or_404(Course, pk=pk)

        registrations = Registration.objects.filter(course=course)

        context = {
            "course": course,
            "registrations": registrations,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):

        course = get_object_or_404(Course, pk=pk)

        registrations = Registration.objects.filter(course=course)

        selected_students = request.POST.getlist("students")

        for registration in registrations:

            Attendance.objects.update_or_create(
                student=registration.student,
                course=course,
                date=date.today(),
                defaults={
                    "present": str(registration.student.id) in selected_students,
                    "marked_by": request.user.lecturer,
                }
            )

        return redirect("lecturer_dashboard")  
    
class AttendanceListView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = "dashboard/attendance_list.html"
    context_object_name = "attendance"

    def get_queryset(self):
        return Attendance.objects.filter(
            marked_by=self.request.user.lecturer
        ).order_by("-date")     
        
class StudentAttendanceView(LoginRequiredMixin, ListView):
    model = Attendance
    template_name = "dashboard/student_attendance.html"
    context_object_name = "attendance"

    def get_queryset(self):
        return Attendance.objects.filter(
            student=self.request.user.student
        ).order_by("-date")
        


class StudentAttendanceSummaryView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/student_attendance_summary.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        student = self.request.user.student

        records = Attendance.objects.filter(student=student).select_related("course")

        summary = defaultdict(lambda: {
            "course__course_code": "",
            "course__course_title": "",
            "total": 0,
            "present": 0,
            "absent": 0,
            "percentage": 0,
        })

        for record in records:
            code = record.course.course_code

            summary[code]["course__course_code"] = record.course.course_code
            summary[code]["course__course_title"] = record.course.course_title

            summary[code]["total"] += 1

            if record.present:
                summary[code]["present"] += 1
            else:
                summary[code]["absent"] += 1

        attendance = list(summary.values())

        for row in attendance:
            row["percentage"] = round(
                (row["present"] / row["total"]) * 100,
                1
            ) if row["total"] else 0

        context["attendance"] = attendance

        return context