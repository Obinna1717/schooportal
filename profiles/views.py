from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from profiles.forms import ProfileForm

from .models import Profile


class ProfileDetailView(
    LoginRequiredMixin,
    DetailView
):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(
    LoginRequiredMixin,
    UpdateView
):
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/edit_profile.html"
    success_url = reverse_lazy("profile")


    def get_object(self):
        return self.request.user.profile