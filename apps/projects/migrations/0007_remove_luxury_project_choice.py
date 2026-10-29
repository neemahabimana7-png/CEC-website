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

class Migration(migrations.Migration):
    dependencies = [("projects", "0006_all_project_galleries")]
    operations = [migrations.AlterField(model_name="projectphoto", name="project_slug", field=models.CharField(max_length=100, choices=CHOICES))]
