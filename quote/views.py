from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from quote.forms import QuoteCreateViewForm
from . import models


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
    model = models.QuoteItem
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

