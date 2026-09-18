from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="team/")
    short_bio = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    legacy_photo_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return self.legacy_photo_url or self.photo.url


class GalleryItem(models.Model):
    image = models.ImageField(upload_to="gallery/")
    legacy_image_url = models.URLField(blank=True)
    title = models.CharField(max_length=200, blank=True)
    caption = models.TextField(blank=True)
    alt_text = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title or f"Gallery image {self.pk}"

    @property
    def image_url(self):
        return self.legacy_image_url or self.image.url