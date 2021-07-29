# Create your views here.
from django.views.generic import DetailView

from . import models


class ViewOrganization(DetailView):
    model = models.OrganizationInfo

    # def get_context_object_name(self, obj):
    #     self.object = 'OrganizationInfo'
