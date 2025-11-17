from rest_framework import generics, permissions

from .models import Application
from .serializers import ApplySerializer, ApplicationSerializer
from .permissions import IsApplicant


class ApplyView(generics.CreateAPIView):
    """
    POST /api/apply/ - apply for a job (applicant only)
    """

    serializer_class = ApplySerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class MyApplicationsView(generics.ListAPIView):
    """
    GET /api/myapplications/ - view my job applications (applicant only)
    """

    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsApplicant]

    def get_queryset(self):
        return Application.objects.filter(applicant=self.request.user).select_related(
            "job"
        )


