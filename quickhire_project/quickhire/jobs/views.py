from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Job
from .serializers import JobSerializer
from .permissions import IsJobOwnerEmployer
from applications.models import Application
from applications.serializers import ApplicationSerializer


class JobListCreateView(generics.ListCreateAPIView):
    """
    GET /api/jobs/ - list all jobs with optional search (?title=&location=)
    POST /api/jobs/ - create job (employer only)
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.query_params.get("title")
        location = self.request.query_params.get("location")
        if title:
            qs = qs.filter(title__icontains=title)
        if location:
            qs = qs.filter(location__icontains=location)
        return qs

    def perform_create(self, serializer):
        user = self.request.user
        if getattr(user, "role", None) != "employer":
            raise PermissionDenied("Only employers can create jobs.")
        serializer.save(posted_by=user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET /api/jobs/<id>/ - retrieve job
    PUT /api/jobs/<id>/ - update job (owner employer only)
    DELETE /api/jobs/<id>/ - delete job (owner employer only)
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated, IsJobOwnerEmployer]


class EmployerApplicantsView(generics.ListAPIView):
    """
    GET /api/employer/applicants/<job_id>/ - view applicants of your job.
    """

    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if getattr(user, "role", None) != "employer":
            raise PermissionDenied("Only employers can view job applicants.")
        job_id = self.kwargs.get("job_id")
        try:
            job = Job.objects.get(id=job_id, posted_by=user)
        except Job.DoesNotExist:
            raise PermissionDenied("You do not own this job or it does not exist.")
        return Application.objects.filter(job=job).select_related("applicant")


