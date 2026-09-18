from django.db import models


PROJECT_CHOICES = (
    ("akagera-game-lodge", "Akagera Game Lodge"),
    ("epca-group-headquarters", "EPCA Group Headquarters"),
    ("keya-nkora-cyimbili-hpp", "Keya, Nkora & Cyimbili HPP Works"),
    ("kanombe-warehouses", "Kanombe Warehouses"),
    ("karongi-quay", "Karongi Auxiliary Quay"),
    ("lebanon-hotel", "Lebanon Hotel (3 Star)"),
    ("luxury-apartments", "Luxury Apartments - Kagarama"),
    ("residential-house-kimihurura", "Residential House - Kimihurura"),
    ("rubavu-port", "Port of Rubavu"),
    ("rusizi-port", "Rusizi Port"),
    ("shango-birembo-transmission", "220kV Shango-Birembo Transmission Line"),
    ("trinity-school", "Trinity International School"),
)


class ProjectPhoto(models.Model):
    project_slug = models.CharField(max_length=100, choices=PROJECT_CHOICES)
    image = models.ImageField(upload_to="projects/")
    alt_text = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return f"{self.get_project_slug_display()} - {self.order}"