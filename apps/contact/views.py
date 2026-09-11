from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "contact/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "contact"
        context["footer_cta"] = "mailto:info@cec.rw"
        return context