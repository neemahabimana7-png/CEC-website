from django.db import migrations

PROJECT = {
    "slug": "kigali-ring-transmission",
    "title": "Kigali Ring 110 kV Transmission Line",
    "description": "Construction of a new 110 kV transmission line from the existing Jabana Substation to a new 110/30 kV substation at Gahanga, supporting reliable distribution of electrical energy in Kigali.",
    "location": "Jabana–Gahanga, Kigali",
    "project_type": "110 kV Transmission Line",
    "status": "Completed",
    "client": "ELTEL Networks Sweden",
    "image_alt": "CEC workers on a transmission tower for the Kigali Ring 110 kV line",
    "category": "power",
    "static_image": "images/Kigali ring.avif"
}
SCOPE = [
    {
        "icon": "bi-map",
        "title": "Topographic Survey",
        "description": "Detailed topographic study of the transmission line route."
    },
    {
        "icon": "bi-signpost-split",
        "title": "Line Route Establishment",
        "description": "Establishment of the route between Jabana and Gahanga."
    },
    {
        "icon": "bi-geo-alt",
        "title": "Tower Foundation Pegging",
        "description": "Pegging of the tower foundation locations along the route."
    },
    {
        "icon": "bi-bricks",
        "title": "Tower Foundations",
        "description": "Construction of foundations for the transmission towers."
    },
    {
        "icon": "bi-tools",
        "title": "Tower Equipment Assembly",
        "description": "Installation and assembly of line tower equipment."
    },
    {
        "icon": "bi-broadcast-pin",
        "title": "Tower Erection",
        "description": "Erection of towers for the new 110 kV transmission line."
    }
]

def seed_project(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Scope = apps.get_model("projects", "ProjectScopeItem")
    data = dict(PROJECT)
    slug = data.pop("slug")
    manager = Project.objects.using(schema_editor.connection.alias)
    project, created = manager.get_or_create(slug=slug, defaults=data)
    if created:
        for order, item in enumerate(SCOPE, 1):
            Scope.objects.using(schema_editor.connection.alias).create(project=project, order=order, **item)

class Migration(migrations.Migration):
    dependencies = [("projects", "0004_seed_street_lighting_project")]
    operations = [migrations.RunPython(seed_project, migrations.RunPython.noop)]
