# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from . import models


class ViewOrganization(DetailView):
    """
     Render a "detail" view of an object.
    """
    model = models.OrganizationInfo


class OrganizationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
        Delete view for delete one of organizations
    """
    model = models.OrganizationInfo
    success_message = "%(name)s was delete successfully"
    success_url = reverse_lazy('dashboard:dashboard')
