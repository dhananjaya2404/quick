from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.ReadOnlyField(source="job.title")
    applicant_username = serializers.ReadOnlyField(source="applicant.username")

    class Meta:
        model = Application
        fields = (
            "id",
            "job",
            "job_title",
            "applicant",
            "applicant_username",
            "resume_link",
            "status",
            "applied_at",
        )
        read_only_fields = ("applicant", "status", "applied_at")


class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ("id", "job", "resume_link", "status", "applied_at")
        read_only_fields = ("status", "applied_at")

    def validate(self, attrs):
        request = self.context.get("request")
        user = getattr(request, "user", None)
        if not user or not user.is_authenticated:
            raise serializers.ValidationError("Authentication required.")
        if getattr(user, "role", None) != "applicant":
            raise serializers.ValidationError("Only applicants can apply for jobs.")

        job = attrs.get("job")
        if Application.objects.filter(job=job, applicant=user).exists():
            raise serializers.ValidationError("You have already applied to this job.")
        return attrs

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        return Application.objects.create(applicant=user, **validated_data)


