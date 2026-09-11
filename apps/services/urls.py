from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.ServicesListView.as_view(), name="list"),
    path("<slug:slug>/", views.LegacyServiceDetailView.as_view(), name="legacy"),
]