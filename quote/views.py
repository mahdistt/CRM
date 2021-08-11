from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from CrmProject import settings
from quote.forms import QuoteCreateViewForm
from . import models


class QuoteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
        Create quote with some items
    """
    model = models.QuoteItem
    form_class = QuoteCreateViewForm
    template_name = 'create-quote.html'
    success_message = "%(quote)s was register successfully"
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
    paginate_by = 3


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


@login_required
def send_email(request, pk):
    quote_objects = models.Quote.objects.get(pk=pk, creator=request.user)
    if quote_objects:
        content = render_to_string('email-templates.txt', {'object_list': quote_objects})
        receiver = quote_objects.organization_related.email
        sender = settings.EMAIL_HOST_USER
        subject = quote_objects.creator
        mail = send_mail(subject, content, sender, [receiver], fail_silently=False)
        if mail:

            messages.success(request, 'Email has been sent.')
            return redirect('quote:list-quote')
        else:
            return HttpResponse('message not sent')
    else:
        return HttpResponse('message not sent')
