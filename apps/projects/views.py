from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from .catalog import PROJECT_DETAILS
from .legacy import PROJECT_FILES, PROJECT_TEMPLATES
from .models import ProjectPhoto, Project

_SLUG_BY_FILE = {v: k for k, v in PROJECT_FILES.items()}


class ProjectsListView(TemplateView):
    template_name = "projects/project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "projects"
        context["footer_cta"] = reverse("contact:contact")
        projects = dict(PROJECT_DETAILS)
        projects.update({p.slug: p.as_catalog_entry() for p in Project.objects.prefetch_related("scope_items")})
        context["additional_projects"] = projects.values()
        return context


class LegacyProjectDetailView(TemplateView):
    """Renders an original project detail page as a Django template."""

    def get_template_names(self):
        if self.kwargs["slug"] in PROJECT_DETAILS or Project.objects.filter(slug=self.kwargs["slug"]).exists():
            return ["projects/project_detail.html"]
        return [PROJECT_TEMPLATES[self.kwargs["slug"]]]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "projects"
        context["footer_cta"] = "mailto:info@cec.rw"
        editable = Project.objects.prefetch_related("scope_items").filter(slug=self.kwargs["slug"]).first()
        context["project"] = editable.as_catalog_entry() if editable else PROJECT_DETAILS.get(self.kwargs["slug"])
        context["project_photos"] = ProjectPhoto.objects.filter(
            project_slug=self.kwargs["slug"], is_active=True
        )
        return context


def legacy_project_redirect(request, file):
    """Redirects old /allprojectsdetails.html/<file>.html URLs to clean slugs."""
    slug = _SLUG_BY_FILE.get(file)
    if slug is None:
        raise Http404
    return HttpResponseRedirect(reverse("projects:legacy", kwargs={"slug": slug}))