from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView, DetailView

from quote.forms import QuoteCreateViewForm
from . import models
from . import celery_tasks


class QuoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
        Create quote with some items
    """
    model = models.QuoteItem
    form_class = QuoteCreateViewForm
    template_name = 'create-quote.html'
    success_message = "%(quote) was register successfully"
    success_url = reverse_lazy('dashboard:dashboard')


#####
# SuccessMessageMixin bala ro ok to template
####
class QuoteListView(LoginRequiredMixin, ListView):
    """
    Show all quotes created by the operator
    """
    model = models.Quote
    template_name = 'list-quote.html'
    paginate_by = 5


class QuoteDetailView(LoginRequiredMixin, DetailView):
    """
    Show a "detail" view of an Quote (calculate).
    """
    model = models.Quote
    template_name = 'detail-quote.html'


class QuotePDFView(LoginRequiredMixin, DetailView):
    """
    Convert quote to pdf
    """
    model = models.Quote
    template_name = 'pdf-quote.html'


@require_http_methods(["GET"])
@login_required
def send_email(request, pk):
    """
    send quote to organization by email
    """
    quote_objects = models.Quote.objects.get(pk=pk, creator=request.user)
    if quote_objects:
        template = render_to_string('email-templates.txt', {'object_list': quote_objects})
        organization_email = quote_objects.organization_related.email
        operator = request.user
        celery_tasks.sed_email_celery.delay(template, operator, organization_email)
        messages.success(request, 'The email send successfully.')
        return redirect(reverse_lazy('quote:list-quotes'))
    else:
        messages.error(request, 'error, tyr again')
        return redirect(reverse_lazy('quote:list-quotes'))
