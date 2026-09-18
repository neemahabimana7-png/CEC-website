from django.contrib import admin
from django.utils.html import format_html

from .models import GalleryItem, TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "name", "role", "order", "is_active", "updated_at")
    list_editable = ("order", "is_active")
    search_fields = ("name", "role", "short_bio")
    list_filter = ("is_active",)
    ordering = ("order", "name")
    fieldsets = (
        ("Team member", {"fields": ("name", "role", "photo", "short_bio", "legacy_photo_url")}),
        ("Publication", {"fields": ("order", "is_active")}),
    )

    def save_model(self, request, obj, form, change):
        if change and "photo" in form.changed_data:
            obj.legacy_photo_url = ""
        super().save_model(request, obj, form, change)

    @admin.display(description="Photo")
    def image_preview(self, obj):
        return format_html(
            '<img src="{}" width="56" height="56" style="object-fit: cover; border-radius: 4px;">',
            obj.image_url,
        )


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ("image_preview", "title", "category", "order", "is_active", "updated_at")
    list_editable = ("order", "is_active")
    search_fields = ("title", "caption", "alt_text")
    list_filter = ("category", "is_active")
    ordering = ("order", "-created_at")
    fieldsets = (
        ("Image", {"fields": ("image", "legacy_image_url", "title", "caption", "alt_text", "category")}),
        ("Publication", {"fields": ("order", "is_active")}),
    )

    @admin.display(description="Image")
    def image_preview(self, obj):
        return format_html(
            '<img src="{}" width="72" height="52" style="object-fit: cover; border-radius: 4px;">',
            obj.image_url,
        )