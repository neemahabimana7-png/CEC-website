from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.db import migrations


PROJECT_PHOTOS = {
    "akagera-game-lodge": [("akagera-game-lodge.jpg", "Akagera Game Lodge")],
    "epca-group-headquarters": [("cec-about-reference.png", "EPCA Group Headquarters")],
    "keya-nkora-cyimbili-hpp": [
        ("nkora-mhpp.jpg", "Nkora MHPP exterior view"),
        ("keya-hpp.jpg", "Hydropower intake and waterway structure"),
        ("cyimbili-mhpp.jpg", "Cyimbili MHPP exterior view"),
    ],
    "kanombe-warehouses": [
        ("cyimbili-mhpp.jpg", "Kanombe Warehouses project image 1"),
        ("nkora-mhpp.jpg", "Kanombe Warehouses project image 2"),
        ("keya-hpp.jpg", "Kanombe Warehouses project image 3"),
    ],
    "karongi-quay": [("Marineservice.jpg", "Karongi Auxiliary Quay construction")],
    "lebanon-hotel": [
        ("rubavu2.PNG", "Lebanon Hotel gallery image 1"),
        ("rubavu3.PNG", "Lebanon Hotel gallery image 2"),
        ("rubavu4.PNG", "Lebanon Hotel gallery image 3"),
        ("rubavu5.PNG", "Lebanon Hotel gallery image 4"),
        ("cec-about-reference.png", "Lebanon Hotel gallery image 5"),
        ("B58A4353.jpg", "Lebanon Hotel gallery image 6"),
    ],
    "luxury-apartments": [
        ("luxury-apartments-blocks.jpg", "Overall view of the Luxury Apartments development"),
        ("luxury-apartments-pool.png", "Swimming pool area at the Luxury Apartments development"),
    ],
    "residential-house-kimihurura": [
        ("residential-house-kimihurura.jpg", "Residential house and swimming pool in Kimihurura"),
    ],
    "rubavu-port": [
        ("rubavu port.jpg", "Completed Port of Rubavu waterfront"),
        ("rubavu2.PNG", "Port of Rubavu cargo quay and vessels"),
        ("rubavu3.PNG", "Port of Rubavu shoreline and road network"),
        ("rubavu4.PNG", "Aerial view of the completed Port of Rubavu"),
        ("rubavu5.PNG", "Port of Rubavu quay and infrastructure"),
        ("Capture.PNG", "Port infrastructure, quay and waterfront"),
    ],
    "rusizi-port": [
        ("RUSIZI1.jpg", "Aerial view of Rusizi Port development in Rwanda"),
        ("RUSIZI2.png", "Aerial view of Rusizi Port development in Rwanda"),
        ("RUSIZI3.jpg", "Aerial view of Rusizi Port development in Rwanda"),
        ("RUSIZI4.png", "Rusizi Port development"),
        ("RUSIZI6.jpg", "Rusizi Port development"),
        ("RUSIZI7.jpg", "Rusizi Port development"),
        ("RUSIZI8.jpg", "Rusizi Port development"),
        ("RUSIZI9.jpg", "Rusizi Port development"),
    ],
    "shango-birembo-transmission": [
        (f"shango-gallery-{index}.jpg", "Transmission infrastructure works")
        for index in range(1, 7)
    ],
    "trinity-school": [
        ("rubavu3.PNG", "Trinity International School gallery image 1"),
        ("cec-about-reference.png", "Trinity International School gallery image 2"),
        ("rubavu4.PNG", "Trinity International School gallery image 3"),
        ("rubavu5.PNG", "Trinity International School gallery image 4"),
        ("B58A4353.jpg", "Trinity International School gallery image 5"),
        ("Capture.PNG", "Trinity International School gallery image 6"),
    ],
}


def seed_project_photos(apps, schema_editor):
    photo_model = apps.get_model("projects", "ProjectPhoto")
    static_images = Path(settings.BASE_DIR) / "static" / "images"

    for project_slug, photos in PROJECT_PHOTOS.items():
        for order, (filename, alt_text) in enumerate(photos):
            source = static_images / filename
            with source.open("rb") as image_file:
                photo_model.objects.create(
                    project_slug=project_slug,
                    image=File(image_file, name=filename),
                    alt_text=alt_text,
                    order=order,
                )


def unseed_project_photos(apps, schema_editor):
    apps.get_model("projects", "ProjectPhoto").objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("projects", "0001_initial")]
    operations = [migrations.RunPython(seed_project_photos, unseed_project_photos)]