from django.db import migrations

PROJECT = {'slug': 'huye-gisagara-gasarenda-kitabi-street-lighting',
 'title': 'Huye–Gisagara & Gasarenda–Kitabi Street Lighting Projects',
 'title_highlight': 'Street Lighting Projects',
 'description': 'CEC carried out street lighting works along Huye–Gisagara '
                'Road and Gasarenda–Kitabi Road under framework contracts for '
                'the construction of MV and LV electrical lines, service '
                'connections, and associated works, including associated civil '
                'works for the Gasarenda–Kitabi project.',
 'location': 'Huye–Gisagara & Gasarenda–Kitabi, Rwanda',
 'project_type': 'Street Lighting / MV & LV Electrical Lines',
 'status': 'Completed',
 'client': 'EDCL — Energy Development Corporation Limited',
 'image_alt': 'Roadside street-lighting poles in Rwanda',
 'category': 'power',
 'static_image': 'images/Street lighting.jpg (1).jpeg'}
SCOPE = [{'icon': 'bi-map',
  'title': 'Line Surveying',
  'description': 'Line surveying for the Huye–Gisagara and Gasarenda–Kitabi '
                 'projects.'},
 {'icon': 'bi-tools',
  'title': 'Excavation for Pole Foundations',
  'description': 'Excavation for pole foundations along both project routes.'},
 {'icon': 'bi-signpost',
  'title': 'Erection of Poles',
  'description': 'Erection of poles for the electrical lines and street '
                 'lighting works.'},
 {'icon': 'bi-bezier2',
  'title': 'Stringing Works',
  'description': 'Stringing works for the electrical lines on both projects.'},
 {'icon': 'bi-lamp',
  'title': 'Installation of Lamps',
  'description': 'Installation of 278 LED streetlights along Huye–Gisagara '
                 'Road and 283 LED streetlights along the 9.9 km '
                 'Gasarenda–Kitabi project.'},
 {'icon': 'bi-hdd-network',
  'title': 'Transformers (Huye–Gisagara)',
  'description': 'Four transformers included in the Huye–Gisagara project.'},
 {'icon': 'bi-broadcast-pin',
  'title': 'Medium Voltage (MV) Line — Huye–Gisagara',
  'description': '1.73 km of Medium Voltage electrical line.'},
 {'icon': 'bi-signpost-split',
  'title': 'Low Voltage (LV) Lines — Huye–Gisagara',
  'description': '9.76 km of Low Voltage electrical lines.'},
 {'icon': 'bi-camera-video',
  'title': 'Security Cameras — Gasarenda–Kitabi',
  'description': 'Installation of security cameras as part of the associated '
                 'works.'},
 {'icon': 'bi-gear',
  'title': 'Commissioning',
  'description': 'Commissioning works for the electrical lines and street '
                 'lighting installations on both projects.'}]


def seed_project(apps, schema_editor):
    Project = apps.get_model("projects", "Project")
    Scope = apps.get_model("projects", "ProjectScopeItem")
    data = dict(PROJECT)
    slug = data.pop("slug")
    project, created = Project.objects.using(schema_editor.connection.alias).get_or_create(slug=slug, defaults=data)
    if created:
        for order, item in enumerate(SCOPE, 1):
            Scope.objects.using(schema_editor.connection.alias).create(project=project, order=order, **item)


class Migration(migrations.Migration):
    dependencies = [("projects", "0003_project_projectscopeitem")]
    operations = [migrations.RunPython(seed_project, migrations.RunPython.noop)]
