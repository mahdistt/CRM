from django.contrib.auth import logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy


# login with class base view
from django.views.generic import UpdateView


class AdminLogoutView(LogoutView):
    template_name = 'LogoutView_form.html'
    success_url = reverse_lazy('users:login')


class AdminLoginView(LoginView):
    template_name = 'LoginView_form.html'
    success_url = reverse_lazy('dashboard:dashboard')


class EditProfile(LoginRequiredMixin, UpdateView):
    """
    Updates a user profile
    """
    model = get_user_model()
    fields = (
        'first_name',
        'last_name',
        'email',
    )
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('dashboard:dashboard')

    def get_object(self, queryset=None):
        return self.request.user
