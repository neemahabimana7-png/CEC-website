from pathlib import Path
from django.conf import settings
from django.core.files import File
from django.db import migrations, models

CHOICES = [
    [
        "shango-birembo-transmission",
        "220kV Shango–Birembo Transmission Line"
    ],
    [
        "akagera-game-lodge",
        "Akagera Game Lodge"
    ],
    [
        "camp-belge-transmission",
        "Camp Belge 30 kV Transmission Line"
    ],
    [
        "epc-west",
        "EPC West"
    ],
    [
        "epca-group-headquarters",
        "EPCA Group Headquarters"
    ],
    [
        "huye-gisagara-gasarenda-kitabi-street-lighting",
        "Huye–Gisagara & Gasarenda–Kitabi Street Lighting Projects"
    ],
    [
        "kanombe-warehouses",
        "Kanombe Warehouses"
    ],
    [
        "karongi-quay",
        "Karongi Auxiliary Quay"
    ],
    [
        "keya-warehouse",
        "Keya Warehouse"
    ],
    [
        "keya-nkora-cyimbili-hpp",
        "Keya, Nkora & Cyimbili HPP Works"
    ],
    [
        "kigali-ring-transmission",
        "Kigali Ring 110 kV Transmission Line"
    ],
    [
        "kilinda-substation",
        "Kilinda Substation Upgrade Project"
    ],
    [
        "lebanon-hotel",
        "Lebanon Hotel (3 Star)"
    ],
    [
        "luxury-apartments",
        "Luxury Apartments – Kagarama"
    ],
    [
        "productive-users",
        "MV & LV Lines for Productive Users"
    ],
    [
        "nyabarongo-substation",
        "Nyabarongo Substation"
    ],
    [
        "rubavu-port",
        "Port of Rubavu"
    ],
    [
        "residential-house-kimihurura",
        "Residential House – Kimihurura"
    ],
    [
        "rusizi-port",
        "Rusizi Port"
    ],
    [
        "trinity-school",
        "Trinity International School"
    ]
]

def seed_gallery(apps, schema_editor):
    Photo = apps.get_model("projects", "ProjectPhoto")
    manager = Photo.objects.using(schema_editor.connection.alias)
    slug = "nyabarongo-substation"
    if not manager.filter(project_slug=slug).exists():
        source = Path(settings.BASE_DIR) / "static/images/Nyabarongo substation.avif"
        if source.exists():
            photo = Photo(project_slug=slug, alt_text="Transformer and workers at Nyabarongo Substation", order=1)
            with source.open("rb") as stream:
                photo.image.save(source.name, File(stream), save=False)
            photo.save(using=schema_editor.connection.alias)

class Migration(migrations.Migration):
    dependencies = [("projects", "0005_seed_kigali_ring_project")]
    operations = [
        migrations.AlterField(model_name="projectphoto", name="project_slug", field=models.CharField(max_length=100, choices=CHOICES)),
        migrations.RunPython(seed_gallery, migrations.RunPython.noop),
    ]
