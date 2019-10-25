from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from accounts.forms import RegistrationForm


class UserProfile(TemplateView):
    template_name = 'accounts/profile.html'


class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
