from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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
    pass
