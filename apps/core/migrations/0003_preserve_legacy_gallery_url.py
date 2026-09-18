from django.db import migrations


LEGACY_EPCA_IMAGE = (
    "https://static.wixstatic.com/media/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg/"
    "v1/fill/w_1200,h_650,al_c,q_90,enc_avif,quality_auto/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg"
)


def preserve_legacy_gallery_url(apps, schema_editor):
    GalleryItem = apps.get_model("core", "GalleryItem")
    GalleryItem.objects.filter(title="EPCA Group Headquarters").update(
        legacy_image_url=LEGACY_EPCA_IMAGE
    )


class Migration(migrations.Migration):
    dependencies = [("core", "0002_seed_content")]
    operations = [migrations.RunPython(preserve_legacy_gallery_url, migrations.RunPython.noop)]