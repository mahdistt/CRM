from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy


# login with class base view

class AdminLogoutView(LogoutView):
    template_name = 'LogoutView_form.html'
    success_url = reverse_lazy('users:login')


class AdminLoginView(LoginView):
    template_name = 'LoginView_form.html'
    success_url = reverse_lazy('dashboard:dashboard')


# def test(request):
#     return render(request, 'LoginView_form.html')

# def logout_view(request):
#     logout(request)
#     return render(request, 'LoginView_form.html')
#
# class EditProfile(LoginRequiredMixin, UpdateView):
#     """
#     Updates a user profile
#     """
#     model = get_user_model()
#     fields = (
#         'first_name',
#         'last_name',
#         'email'
#     )
#     template_name = 'phones/edit_profile.html'
#     success_url = reverse_lazy('phones:home')
#
#     def get_object(self, queryset=None):
#         return self.request.user
