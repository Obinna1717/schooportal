from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)

from django.shortcuts import get_object_or_404, redirect
from accounts.mixins import LecturerRequiredMixin, StudentRequiredMixin
from .models import Course, Registration


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"


class CourseCreateView(
    LoginRequiredMixin,
    LecturerRequiredMixin,
    CreateView
):
    model = Course

    fields = [
        "course_code",
        "course_title",
        "units",
        "semester",
        "department",
        "lecturer",
    ]

    template_name = "courses/course_form.html"
    success_url = reverse_lazy("course_list")


class CourseUpdateView(
    LoginRequiredMixin,
    LecturerRequiredMixin,
    UpdateView
):
    model = Course

    fields = [
        "course_code",
        "course_title",
        "units",
        "semester",
        "department",
        "lecturer",
    ]

    template_name = "courses/course_form.html"
    success_url = reverse_lazy("course_list")


class CourseDeleteView(
    LoginRequiredMixin,
    LecturerRequiredMixin,
    DeleteView
):
    model = Course
    template_name = "courses/course_confirm_delete.html"
    success_url = reverse_lazy("course_list")


class MyCoursesView(
    LoginRequiredMixin,
    StudentRequiredMixin,
    ListView
):
    model = Registration
    template_name = "courses/my_courses.html"
    context_object_name = "registrations"

    def get_queryset(self):
        return Registration.objects.filter(
            student=self.request.user.student
        )


class RegisterCourseView(
    LoginRequiredMixin,
    StudentRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(
            Course,
            pk=kwargs["pk"]
        )

        Registration.objects.get_or_create(
            student=request.user.student,
            course=course,
            session="2025/2026"
        )

        return redirect("course_list")