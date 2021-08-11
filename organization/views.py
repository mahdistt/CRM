# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models, serializers


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


class OrganizationInfoAPI(ListAPIView):
    """
    API  all organizations related with operator (JWT)
    """
    serializer_class = serializers.OrganizationSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = models.OrganizationInfo.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(created_info=self.request.user)
