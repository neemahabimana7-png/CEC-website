from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from .models import ProjectPhoto


PNG_BYTES = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\x0dIDAT\x08\xd7c\xf8\xcf\xc0\xf0\x1f\x00\x05\x00\x01\xff\x89\x99=\x1d"
    b"\x00\x00\x00\x00IEND\xaeB`\x82"
)


def uploaded_image(name="project.png"):
    return SimpleUploadedFile(name, PNG_BYTES, content_type="image/png")


class ProjectPhotoTests(TestCase):
    def test_project_photo_can_be_created_and_ordered(self):
        ProjectPhoto.objects.all().delete()
        later = ProjectPhoto.objects.create(
            project_slug="rubavu-port", image=uploaded_image("later.png"), order=2
        )
        first = ProjectPhoto.objects.create(
            project_slug="rubavu-port", image=uploaded_image("first.png"), order=1
        )

        self.assertEqual(list(ProjectPhoto.objects.all()), [first, later])

    def test_only_active_photos_for_requested_project_are_rendered(self):
        ProjectPhoto.objects.all().delete()
        visible = ProjectPhoto.objects.create(
            project_slug="rubavu-port",
            image=uploaded_image("visible.png"),
            alt_text="Visible project photo",
        )
        ProjectPhoto.objects.create(
            project_slug="rusizi-port",
            image=uploaded_image("other.png"),
            alt_text="Other project photo",
        )
        ProjectPhoto.objects.create(
            project_slug="rubavu-port",
            image=uploaded_image("hidden.png"),
            alt_text="Hidden project photo",
            is_active=False,
        )

        response = self.client.get(
            reverse("projects:legacy", kwargs={"slug": "rubavu-port"})
        )

        self.assertContains(response, visible.alt_text)
        self.assertNotContains(response, "Other project photo")
        self.assertNotContains(response, "Hidden project photo")

    def test_existing_project_content_remains_present(self):
        response = self.client.get(
            reverse("projects:legacy", kwargs={"slug": "shango-birembo-transmission"})
        )

        self.assertContains(response, "220kV Shango–Birembo Transmission Line")
        self.assertContains(response, "Route Survey &amp; Tower Pegging")


class ProjectTemplateContentTests(TestCase):
    def test_all_project_pages_render_from_legacy_templates(self):
        from .legacy import PROJECT_TEMPLATES
        for slug, template in PROJECT_TEMPLATES.items():
            with self.subTest(slug=slug):
                response = self.client.get(reverse("projects:legacy", kwargs={"slug": slug}))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, template)

    def test_database_content_does_not_override_html(self):
        from .models import Project
        Project.objects.filter(slug="kigali-ring-transmission").update(client="Database override")
        response = self.client.get(reverse("projects:legacy", kwargs={"slug": "kigali-ring-transmission"}))
        self.assertContains(response, "ELTEL Networks Sweden")
        self.assertNotContains(response, "Database override")

    def test_camp_belge_client_and_gallery_are_connected(self):
        photo = ProjectPhoto.objects.create(project_slug="camp-belge-transmission", image=uploaded_image("camp-gallery.png"), alt_text="Camp Belge gallery verification")
        self.addCleanup(photo.image.delete, save=False)
        response = self.client.get(reverse("projects:legacy", kwargs={"slug": "camp-belge-transmission"}))
        self.assertContains(response, "EDCL")
        self.assertContains(response, photo.alt_text)

    def test_gallery_selection_covers_every_project(self):
        from .legacy import PROJECT_TEMPLATES
        from .models import PROJECT_CHOICES
        self.assertEqual(set(dict(PROJECT_CHOICES)), set(PROJECT_TEMPLATES))

    def test_project_list_contains_each_project_once(self):
        from .legacy import PROJECT_TEMPLATES
        response = self.client.get(reverse("projects:list"))
        for slug in PROJECT_TEMPLATES:
            url = reverse("projects:legacy", kwargs={"slug": slug})
            self.assertContains(response, 'href="' + url + '"', count=1)
