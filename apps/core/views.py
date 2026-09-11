from django.urls import reverse
from django.views.generic import TemplateView


class PageView(TemplateView):
    """Shared context (active nav item, footer CTA link) for CEC pages."""

    active_nav = ""
    footer_cta = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = self.active_nav
        context["footer_cta"] = self.footer_cta
        return context


class HomeView(PageView):
    template_name = "core/home.html"
    active_nav = "home"


class AboutView(PageView):
    template_name = "core/about.html"
    active_nav = "about"


class CareersView(TemplateView):
    template_name = "core/careers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "careers"
        context["footer_cta"] = reverse("contact:contact")
        return context


class ClientsView(PageView):
    template_name = "core/clients.html"
    active_nav = "clients"