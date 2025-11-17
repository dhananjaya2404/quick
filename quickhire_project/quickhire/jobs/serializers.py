from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    posted_by = serializers.ReadOnlyField(source="posted_by.username")

    class Meta:
        model = Job
        fields = (
            "id",
            "title",
            "description",
            "salary",
            "location",
            "posted_by",
            "created_at",
        )


