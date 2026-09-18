from django.views.generic import TemplateView

from apps.core.models import GalleryItem


class NewsListView(TemplateView):
    template_name = "news/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "news"
        context["footer_cta"] = "mailto:info@cec.rw"
        context["gallery_items"] = [
            {
                "image": item.image_url,
                "name": item.title or "CEC gallery image",
                "category": item.category,
                "alt": item.alt_text or item.title or "CEC gallery image",
            }
            for item in GalleryItem.objects.filter(is_active=True)
        ]
        return context


class NewsArticleView(TemplateView):
    template_name = "news/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "news"
        context["footer_cta"] = "mailto:info@cec.rw"
        return context