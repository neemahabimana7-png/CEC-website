from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectsListView.as_view(), name="list"),
    path("<slug:slug>/", views.LegacyProjectDetailView.as_view(), name="legacy"),
]