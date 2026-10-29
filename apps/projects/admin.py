from django.contrib import admin
from django.utils.html import format_html

from .models import ProjectPhoto, PROJECT_CHOICES


@admin.register(ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(project_slug__in=[slug for slug, _ in PROJECT_CHOICES])

    list_display = ("image_preview", "project_slug", "order", "is_active", "updated_at")
    list_editable = ("order", "is_active")
    search_fields = ("alt_text", "project_slug")
    list_filter = ("project_slug", "is_active")
    ordering = ("project_slug", "order", "-created_at")
    fieldsets = (
        ("Project photo", {"fields": ("project_slug", "image", "alt_text")}),
        ("Publication", {"fields": ("order", "is_active")}),
    )

    @admin.display(description="Preview")
    def image_preview(self, obj):
        return format_html(
            '<img src="{}" width="72" height="52" style="object-fit: cover; border-radius: 4px;">',
            obj.image.url,
        )
