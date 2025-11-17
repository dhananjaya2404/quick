from django.urls import path

from .views import ApplyView, MyApplicationsView

urlpatterns = [
    path("apply/", ApplyView.as_view(), name="apply"),
    path("myapplications/", MyApplicationsView.as_view(), name="my-applications"),
]


