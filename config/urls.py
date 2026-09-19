"""
Root URL configuration for the CEC website.

Clean (canonical) URLs are served by the Django templates. The original
static-site .html paths are kept as permanent redirects to the new URLs so
existing bookmarks and links keep working.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.views.static import serve

from apps.projects import views as project_views
from apps.services import views as service_views

urlpatterns = [
    path("", include("apps.core.urls")),
    path("contact/", include("apps.contact.urls")),
    path("news/", include("apps.news.urls")),
    path("services/", include("apps.services.urls")),
    path("projects/", include("apps.projects.urls")),
    path("admin/", admin.site.urls),
]

# ---- Legacy static-site URL redirects (keep original files untouched) ----
legacy_redirects = [
    path("index.html", RedirectView.as_view(pattern_name="core:home", permanent=True)),
    path(
        "navbar/aboutus.html",
        RedirectView.as_view(pattern_name="core:about", permanent=True),
    ),
    path(
        "navbar/careers.html",
        RedirectView.as_view(pattern_name="core:careers", permanent=True),
    ),
    path(
        "navbar/clients.html",
        RedirectView.as_view(pattern_name="core:clients", permanent=True),
    ),
    path(
        "navbar/contactus.html",
        RedirectView.as_view(pattern_name="contact:contact", permanent=True),
    ),
    path(
        "navbar/news.html",
        RedirectView.as_view(pattern_name="news:list", permanent=True),
    ),
    path(
        "navbar/news-article.html",
        RedirectView.as_view(
            pattern_name="news:detail", query_string=True, permanent=True
        ),
    ),
    path(
        "services/allservices.html",
        RedirectView.as_view(pattern_name="services:list", permanent=True),
    ),
    path(
        "allprojects/allprojects.html",
        RedirectView.as_view(pattern_name="projects:list", permanent=True),
    ),
    path(
        "servicesdetails/<str:file>.html",
        service_views.legacy_service_redirect,
    ),
    path(
        "allprojectsdetails.html/<str:file>.html",
        project_views.legacy_project_redirect,
    ),
]
urlpatterns += legacy_redirects

handler404 = "config.views.handler404"
handler500 = "config.views.handler500"

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path(
            "media/<path:path>",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]