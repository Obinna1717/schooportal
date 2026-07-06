from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from accounts.permissions import is_lecturer

from accounts.permissions import is_student
from courses.models import CourseMaterial

@login_required
@user_passes_test(is_student)
def student_dashboard(request):

    materials = CourseMaterial.objects.all()

    return render(
        request,
        'dashboard/student_dashboard.html',
        {
            'materials': materials
        }
    )

@login_required
@user_passes_test(is_lecturer)
def lecturer_dashboard(request):
    
    materials = CourseMaterial.objects.all()

    return render(
        request,
        'dashboard/lecturer_dashboard.html',
        {
            'materials': materials
        }
    )
    
    return render(request, 'dashboard/lecturer_dashboard.html')

# def role_redirect(request):
#     if request.user.role == "lecturer":
#         return redirect('lecturer_dashboard')
#     elif request.user.role == "student":
#         return redirect('student_dashboard')
#     else:
#         return redirect('login')

from django.http import HttpResponse

def role_redirect(request):
    return HttpResponse(
        f"Login successful! Username: {request.user.username}, Role: {request.user.role}"
    )


class RegisterView(
    CreateView
):

    form_class = RegisterForm

    template_name = 'accounts/register.html'

    success_url = reverse_lazy(
        'login'
    )
    
    