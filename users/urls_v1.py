from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from users.views import RegistrationAPIView


urlpatterns = [
    path("login", TokenObtainPairView.as_view()),
    path("registration", RegistrationAPIView.as_view()),
]
