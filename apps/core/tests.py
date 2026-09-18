from django.contrib import admin
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from apps.projects.models import ProjectPhoto

from .models import GalleryItem, TeamMember


PNG_BYTES = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01"
    b"\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89"
    b"\x00\x00\x00\x0dIDAT\x08\xd7c\xf8\xcf\xc0\xf0\x1f\x00\x05\x00\x01\xff\x89\x99=\x1d"
    b"\x00\x00\x00\x00IEND\xaeB`\x82"
)


def uploaded_image(name="content.png"):
    return SimpleUploadedFile(name, PNG_BYTES, content_type="image/png")


class TeamMemberTests(TestCase):
    def test_string_representation_returns_name(self):
        member = TeamMember.objects.create(name="Ada Lovelace", role="Engineer", photo=uploaded_image())

        self.assertEqual(str(member), "Ada Lovelace")

    def test_team_member_can_be_created_and_ordered(self):
        TeamMember.objects.all().delete()
        later = TeamMember.objects.create(name="Later", role="Engineer", photo=uploaded_image("later.png"), order=2)
        first = TeamMember.objects.create(name="First", role="Director", photo=uploaded_image("first.png"), order=1)

        self.assertEqual(list(TeamMember.objects.all()), [first, later])

    def test_about_shows_active_members_only(self):
        TeamMember.objects.all().delete()
        active = TeamMember.objects.create(name="Visible", role="Director", photo=uploaded_image())
        TeamMember.objects.create(name="Hidden", role="Engineer", photo=uploaded_image("hidden.png"), is_active=False)

        response = self.client.get(reverse("core:about"))

        self.assertContains(response, active.name)
        self.assertNotContains(response, "Hidden")
        self.assertContains(response, active.photo.url)

    def test_about_renders_active_members_in_order(self):
        TeamMember.objects.all().delete()
        first = TeamMember.objects.create(name="First", role="Director", photo=uploaded_image("first.png"), order=1)
        second = TeamMember.objects.create(name="Second", role="Engineer", photo=uploaded_image("second.png"), order=2)

        response = self.client.get(reverse("core:about"))

        self.assertLess(response.content.index(first.name.encode()), response.content.index(second.name.encode()))

    def test_about_renders_when_no_members_exist(self):
        TeamMember.objects.all().delete()

        response = self.client.get(reverse("core:about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "team-row")


class GalleryItemTests(TestCase):
    def test_gallery_item_can_be_created_and_ordered(self):
        GalleryItem.objects.all().delete()
        later = GalleryItem.objects.create(title="Later", image=uploaded_image("later.png"), order=2)
        first = GalleryItem.objects.create(title="First", image=uploaded_image("first.png"), order=1)

        self.assertEqual(list(GalleryItem.objects.all()), [first, later])

    def test_active_gallery_item_is_rendered_with_image_url(self):
        GalleryItem.objects.all().delete()
        item = GalleryItem.objects.create(
            title="Visible gallery item",
            alt_text="Visible image",
            category="Projects",
            image=uploaded_image(),
        )

        response = self.client.get(reverse("news:list"))

        self.assertContains(response, item.title)
        self.assertContains(response, item.image.url)

    def test_inactive_gallery_item_is_not_rendered(self):
        GalleryItem.objects.all().delete()
        GalleryItem.objects.create(title="Hidden gallery item", image=uploaded_image(), is_active=False)

        response = self.client.get(reverse("news:list"))

        self.assertNotContains(response, "Hidden gallery item")


class AdminRegistrationTests(TestCase):
    def test_content_models_are_registered(self):
        self.assertIn(TeamMember, admin.site._registry)
        self.assertIn(GalleryItem, admin.site._registry)
        self.assertIn(ProjectPhoto, admin.site._registry)

    def test_team_admin_changelist_and_add_pages_are_available(self):
        admin_user = self._create_admin_user()
        self.client.force_login(admin_user)

        changelist = self.client.get(reverse("admin:core_teammember_changelist"))
        add_page = self.client.get(reverse("admin:core_teammember_add"))

        self.assertEqual(changelist.status_code, 200)
        self.assertEqual(add_page.status_code, 200)

    def _create_admin_user(self):
        from django.contrib.auth import get_user_model

        return get_user_model().objects.create_superuser(
            username="team-admin",
            email="team-admin@example.com",
            password="test-password-123",
        )