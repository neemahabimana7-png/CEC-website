from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("careers/", views.CareersView.as_view(), name="careers"),
    path("clients/", views.ClientsView.as_view(), name="clients"),
]