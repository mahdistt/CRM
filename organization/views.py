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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.setdefault("related", models.OrganizationProduct.objects)
    #     return context


class OrganizationDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
        Delete view for delete one of organizations
    """
    model = models.OrganizationInfo
    success_message = "%(name) was delete successfully"
    success_url = reverse_lazy('dashboard:dashboard')

#
# class ViewRelatedProduct(DetailView):
#     """
#      Render related product with id in URL
#     """
#     model = models.OrganizationInfo

#
# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['related_object_bk'] = [range(10)]
# context['related_object_bk'] = models.OrganizationInfo.objects.filter(id__in=[1,2,3,4,5])
# return context
# context['related_object_bk'] = models.Product.ProductInfo.objects.filter(
#     organizationproduct__related_product__in=models.OrganizationProduct)
# def get_context_object_name(self, obj):
#     self.object = 'OrganizationInfo'
# def get_context_data(self, **kwargs):
#     related_product = instance_product.ProductInfo.objects.filter(organita)
