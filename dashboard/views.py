import itertools

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from dashboard.forms import OrganizationRegisterForm
from organization import models


# Create your views here.
@login_required
def show_dashboard(request):
    """
    Display special organization information for each operator
    """
    if request.user.is_authenticated:
        if not request.user.is_superuser:
            operator_organization = models.OrganizationInfo.objects.filter(operator_info=request.user)
        else:
            operator_organization = models.OrganizationInfo.objects.all()
        other_number = []
        qs = list(itertools.chain(operator_organization, other_number))
        paginated = Paginator(qs, 3)
        paginated_page = paginated.get_page(request.GET.get('page', 1))
        return render(request=request,
                      context={'object_list': paginated_page,
                               },
                      template_name='dashboard/dashboard.html')
    else:
        return render(request, 'dashboard/dashboard.html')


class CreateFormOrganization(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
        Create view for register organizations
    """
    model = models.OrganizationInfo
    form_class = OrganizationRegisterForm
    template_name = 'dashboard/register_organization.html'
    success_message = "%(name) was register successfully"
    success_url = reverse_lazy('dashboard:dashboard')

# Ajax view for register form
# ------------------------------------
# @require_POST
# def get_info_register_form(request):
#     """
#     register organizations by form (AJAX)
#     """
#
#     form_instance = forms.OrganizationRegisterForm(data=request.POST)
#     if not form_instance.is_valid():
#         form_instance.instance.operator_info = request.user
#         form_instance.save()
#         return render(request, 'dashboard/dashboard.html')
#
# ------------------------------------
# @require_GET
# @login_required
# def show_register_organization_form(request):
#     """
#     Show register form by widget tweaks
#     """
#     return render(request, 'dashboard/register_organization.html', {
#         'form_org': forms.OrganizationRegisterForm(),
#     })
# ------------------------------------
