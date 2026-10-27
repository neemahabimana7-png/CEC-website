from django.contrib import admin
from django.utils.html import format_html

from .models import ProjectPhoto, Project, ProjectScopeItem


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

class ProjectScopeInline(admin.TabularInline):
    model = ProjectScopeItem
    extra = 0
    fields = ("order", "title", "description", "icon")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status")
    search_fields = ("title", "location", "client")
    inlines = [ProjectScopeInline]
    readonly_fields = ("slug",)
    fieldsets = (
        ("Project", {"fields": ("slug", "title", "title_highlight", "description", "category")}),
        ("Project information", {"fields": ("location", "project_type", "status", "client")}),
        ("Main photograph", {"fields": ("image", "static_image", "image_alt")}),
    )

    def has_add_permission(self, request):
        return False
