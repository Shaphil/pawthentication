from django.urls import path

from accounts.views import UserProfile, RegistrationView


urlpatterns = [
    path('profile/', UserProfile.as_view(), name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
]
