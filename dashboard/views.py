import itertools

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import DetailView

from organization import models
from . import forms


# Create your views here.
@login_required
def show_dashboard(request):
    # if not request.user.is_superuser:
    if request.user.is_authenticated:
        operator_organization = models.OrganizationInfo.objects.filter(operator_info=request.user)
        other_number = []
        qs = list(itertools.chain(operator_organization, other_number))
        paginated = Paginator(qs, 2)
        paginated_page = paginated.get_page(request.GET.get('page', 1))
        return render(request=request,
                      context={'object_list': paginated_page,
                               'page_obj': 'paginated',
                               },
                      template_name='dashboard/dashboard.html')
    else:
        return render(request, 'dashboard/dashboard.html')


@csrf_exempt
@require_POST
def get_info_register_form(request):
    """
    register organizations by form (AJAX)
    """
    form_instance = forms.OrganizationRegisterForm(data=request.POST)
    if form_instance.is_valid():
        form_instance.instance.operator_info = request.user
        form_instance.save()
        return render(request, 'dashboard/dashboard.html')


@csrf_exempt
@require_GET
@login_required
def show_register_organization_form(request):
    """
    Show register form by widget tweaks
    """
    return render(request, 'dashboard/register_organization.html', {
        'form_org': forms.OrganizationRegisterForm(),
    })

