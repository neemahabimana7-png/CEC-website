from django.views.generic import TemplateView


class NewsListView(TemplateView):
    template_name = "news/article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "news"
        context["footer_cta"] = "mailto:info@cec.rw"
        return context


class NewsArticleView(TemplateView):
    template_name = "news/article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_nav"] = "news"
        context["footer_cta"] = "mailto:info@cec.rw"
        return context