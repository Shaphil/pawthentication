from django.views.generic import TemplateView


class UserProfile(TemplateView):
    template_name = 'accounts/profile.html'
