from django.urls import path

from .views import (
    CourseListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    MyCoursesView,
    RegisterCourseView
)

urlpatterns = [

    path(
        "",
        CourseListView.as_view(),
        name="course_list"
    ),

    path(
        "add/",
        CourseCreateView.as_view(),
        name="course_add"
    ),

    path(
        "<int:pk>/edit/",
        CourseUpdateView.as_view(),
        name="course_update"
    ),

    path(
        "<int:pk>/delete/",
        CourseDeleteView.as_view(),
        name="course_delete"
    ),

    path(
        "my-courses/",
        MyCoursesView.as_view(),
        name="my_courses"
    ),

    path(
        "<int:pk>/register/",
        RegisterCourseView.as_view(),
        name="register_course"
    ),

]