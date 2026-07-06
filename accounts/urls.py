from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)

from .views import RegisterView, lecturer_dashboard, role_redirect, student_dashboard

urlpatterns = [

    path('register/',RegisterView.as_view(),name='register'),

    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),

    path('logout/',LogoutView.as_view(),name='logout'),
    
    path('lecturer-dashboard/', lecturer_dashboard, name='lecturer_dashboard'),
    
    path('student-dashboard/', student_dashboard, name='student_dashboard'),
    
    path('redirect/', role_redirect, name='role_redirect'),

]