from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "location", "salary", "posted_by", "created_at")
    list_filter = ("location", "posted_by")
    search_fields = ("title", "location", "posted_by__username")


