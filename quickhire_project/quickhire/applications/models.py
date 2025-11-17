from django.conf import settings
from django.db import models

from jobs.models import Job


class Application(models.Model):
    STATUS_CHOICES = [
        ("Applied", "Applied"),
        ("Reviewed", "Reviewed"),
        ("Accepted", "Accepted"),
        ("Rejected", "Rejected"),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications",
    )
    resume_link = models.URLField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Applied",
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("job", "applicant")
        ordering = ["-applied_at"]

    def __str__(self) -> str:
        return f"{self.applicant} -> {self.job} ({self.status})"


