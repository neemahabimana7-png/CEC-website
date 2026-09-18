from django.contrib import admin
from django.utils.html import format_html

from .models import ProjectPhoto


@admin.register(ProjectPhoto)
class ProjectPhotoAdmin(admin.ModelAdmin):
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