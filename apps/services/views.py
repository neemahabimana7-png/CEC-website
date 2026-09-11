from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

from .legacy import SERVICE_FILES, SERVICE_TEMPLATES

_SLUG_BY_FILE = {v: k for k, v in SERVICE_FILES.items()}


class ServicesListView(TemplateView):
    template_name = "services/service_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "services"
        context["footer_cta"] = "mailto:info@cec.rw"
        return context


class LegacyServiceDetailView(TemplateView):
    """Renders an original service detail page as a Django template."""

    def get_template_names(self):
        return [SERVICE_TEMPLATES[self.kwargs["slug"]]]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "services"
        context["footer_cta"] = "mailto:info@cec.rw"
        context["data_service_file"] = SERVICE_FILES[self.kwargs["slug"]]
        return context


def legacy_service_redirect(request, file):
    """Redirects old /servicesdetails/<file>.html URLs to clean slugs."""
    slug = _SLUG_BY_FILE.get(file)
    if slug is None:
        raise Http404
    return HttpResponseRedirect(reverse("services:legacy", kwargs={"slug": slug}))