from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, UserSerializer


User = get_user_model()


class APIRootView(APIView):
    """
    GET /api/ - Simple API root listing available endpoints.
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "register": "/api/register/",
                "token_obtain": "/api/token/",
                "token_refresh": "/api/token/refresh/",
                "jobs": "/api/jobs/",
                "apply": "/api/apply/",
                "my_applications": "/api/myapplications/",
            }
        )


class RegisterView(generics.CreateAPIView):
    """
    POST /api/register/ - register a new user.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeView(generics.RetrieveAPIView):
    """
    GET /api/me/ - get the current authenticated user.
    """

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


