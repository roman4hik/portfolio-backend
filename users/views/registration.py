from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import RegistrationSerializer


class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)
