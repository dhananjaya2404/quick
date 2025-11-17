from django.urls import path

from .views import JobListCreateView, JobDetailView, EmployerApplicantsView

urlpatterns = [
    path("jobs/", JobListCreateView.as_view(), name="job-list-create"),
    path("jobs/<int:pk>/", JobDetailView.as_view(), name="job-detail"),
    path(
        "employer/applicants/<int:job_id>/",
        EmployerApplicantsView.as_view(),
        name="employer-applicants",
    ),
]


