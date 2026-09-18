from pathlib import Path

from django.conf import settings
from django.core.files import File
from django.db import migrations


TEAM_MEMBERS = [
    {
        "name": "Ferdy TURASENGA",
        "role": "Executive Chairman",
        "source": "team-photo-placeholder.svg",
        "legacy_photo_url": "https://www.epcafrica.com/assets/team/bord/ferdyturasenga.png",
        "order": 0,
    },
    {
        "name": "Carine KAMANZI",
        "role": "Managing Director",
        "source": "team-photo-placeholder.svg",
        "legacy_photo_url": "https://www.epcafrica.com/assets/team/members/CarineKAMANZI.jpeg",
        "order": 1,
    },
    {
        "name": "Eric MUGWANEZA",
        "role": "Director of Administration and Finance",
        "source": "MUGWANEZA_ERIC-_DAF.jpeg",
        "order": 2,
    },
]

GALLERY_ITEMS = [
    ("B58A4353.jpg", "Shango-Birembo Transmission Line", "Power & Energy"),
    ("cec-about-reference.png", "EPCA Group Headquarters", "Buildings"),
    ("Capture.PNG", "Rubavu Port", "Marine & Civil Works"),
    ("Rusizi port.jpg", "Rusizi Port", "Marine & Civil Works"),
    ("RUSIZI1.jpg", "Rusizi Port - Photo 1", "Marine & Civil Works"),
    ("RUSIZI2.png", "Rusizi Port - Photo 2", "Marine & Civil Works"),
    ("RUSIZI3.jpg", "Rusizi Port - Photo 3", "Marine & Civil Works"),
    ("RUSIZI4.png", "Rusizi Port - Photo 4", "Marine & Civil Works"),
    ("RUSIZI6.jpg", "Rusizi Port - Photo 5", "Marine & Civil Works"),
    ("RUSIZI7.jpg", "Rusizi Port - Photo 6", "Marine & Civil Works"),
    ("RUSIZI8.jpg", "Rusizi Port - Photo 7", "Marine & Civil Works"),
    ("RUSIZI9.jpg", "Rusizi Port - Photo 8", "Marine & Civil Works"),
    ("luxury-apartments-blocks.jpg", "Luxury Apartments - Kagarama", "Buildings"),
    ("akagera-game-lodge.jpg", "Akagera Game Lodge", "Buildings"),
    ("residential-house-kimihurura.jpg", "Kimihurura Residential House", "Buildings"),
    ("keya-hpp.jpg", "Keya Hydropower Plant", "Power & Energy"),
    ("rubavu3.PNG", "Rubavu Port Infrastructure", "Marine & Civil Works"),
]


def seed_content(apps, schema_editor):
    team_model = apps.get_model("core", "TeamMember")
    gallery_model = apps.get_model("core", "GalleryItem")
    static_images = Path(settings.BASE_DIR) / "static" / "images"

    for member in TEAM_MEMBERS:
        member = member.copy()
        source = static_images / member.pop("source")
        with source.open("rb") as image_file:
            team_model.objects.create(
                **member,
                photo=File(image_file, name=source.name),
            )

    for order, (filename, title, category) in enumerate(GALLERY_ITEMS):
        source = static_images / filename
        with source.open("rb") as image_file:
            gallery_model.objects.create(
                title=title,
                alt_text=title,
                category=category,
                order=order,
                legacy_image_url=(
                    "https://static.wixstatic.com/media/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg/"
                    "v1/fill/w_1200,h_650,al_c,q_90,enc_avif,quality_auto/6a77e1_3c205c16feb94b99bff6985abb0ec336~mv2.jpg"
                    if title == "EPCA Group Headquarters"
                    else ""
                ),
                image=File(image_file, name=filename),
            )


def unseed_content(apps, schema_editor):
    apps.get_model("core", "TeamMember").objects.all().delete()
    apps.get_model("core", "GalleryItem").objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("core", "0001_initial")]
    operations = [migrations.RunPython(seed_content, unseed_content)]