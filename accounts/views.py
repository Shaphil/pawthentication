from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from accounts.forms import RegistrationForm


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
