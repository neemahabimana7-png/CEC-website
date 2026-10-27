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

class Project(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    title_highlight = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    project_type = models.CharField(max_length=255)
    status = models.CharField(max_length=100, default="Completed")
    client = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    static_image = models.CharField(max_length=255, blank=True, help_text="Existing image path used until an image is uploaded.")
    image_alt = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=20, choices=[("power", "Energy Projects"), ("buildings", "Buildings"), ("marine", "Marine & Civil"), ("industrial", "Industrial & Infrastructure")], default="power")

    def __str__(self):
        return self.title

    def as_catalog_entry(self):
        prefix = self.title
        highlight = self.title_highlight
        if highlight and prefix.endswith(highlight):
            prefix = prefix[:-len(highlight)].rstrip()
        else:
            highlight = ""
        return dict(slug=self.slug, title=self.title, title_prefix=prefix,
                    title_highlight=highlight, description=self.description,
                    location=self.location, project_type=self.project_type,
                    status=self.status, client=self.client,
                    image=self.static_image, image_url=self.image.url if self.image else "",
                    image_alt=self.image_alt, category=self.category,
                    layout_class="project-street-lighting" if self.slug == "huye-gisagara-gasarenda-kitabi-street-lighting" else "",
                    scope=list(self.scope_items.values("icon", "title", "description")), gallery=[])


class ProjectScopeItem(models.Model):
    project = models.ForeignKey(Project, related_name="scope_items", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=60, default="bi-tools", help_text="Bootstrap icon class, for example bi-lamp.")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "pk"]

    def __str__(self):
        return self.title
