from django.urls import path

from .views import (
    CourseListAPIView,
    CourseCreateAPIView,
    CourseDetailAPIView,
    CourseUpdateAPIView,
    CourseDeleteAPIView,
    PaymentListAPIView,
)

urlpatterns = [
    path(
        "courses/",
        CourseListAPIView.as_view(),
        name="course-list"
    ),

    path(
        "courses/create/",
        CourseCreateAPIView.as_view(),
        name="course-create"
    ),

    path(
        "courses/<int:pk>/",
        CourseDetailAPIView.as_view(),
        name="course-detail"
    ),

    path(
        "courses/<int:pk>/update/",
        CourseUpdateAPIView.as_view(),
        name="course-update"
    ),

    path(
        "courses/<int:pk>/delete/",
        CourseDeleteAPIView.as_view(),
        name="course-delete"
    ),
    
      path(
        'payments/',
        PaymentListAPIView.as_view(),
        name='payment-list'
    ),
]