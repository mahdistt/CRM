from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.views.generic import DetailView, CreateView

from followup import models
from followup.forms import FollowUpCreateForm


class FollowUpCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    model = models.FollowUp
    template_name = 'followup/create-followup.html'
    form_class = FollowUpCreateForm
    success_message = '%(creator_related)s your follow up successfully added'

    def get_form_kwargs(self):
        user_instance_dict = super().get_form_kwargs()
        user_instance_dict.update({'creator_info': self.request.user})
        return user_instance_dict

    def form_invalid(self, form):
        return JsonResponse({'massages': 'invalid data.'}, status=400)

    def form_valid(self, form):
        try:
            form.instance.creator_related = self.request.user
            self.object = form.save()
            return JsonResponse({'massages': 'Created successfully.'}, status=201)
        except:
            return JsonResponse({'massages': 'invalid data.'}, status=400)


class FollowUpDetailView(LoginRequiredMixin, DetailView):
    """
        view for Follow up detail
    """
    model = models.FollowUp
    template_name = 'followup/detail-followup.html'
