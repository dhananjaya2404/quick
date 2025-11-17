from django.urls import path

from .views import APIRootView, RegisterView, MeView

urlpatterns = [
    path("", APIRootView.as_view(), name="api-root"),
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", MeView.as_view(), name="me"),
]



