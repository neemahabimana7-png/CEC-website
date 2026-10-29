# Editing projects

- Edit project titles, descriptions, metadata, main photographs and scope cards in legacy/<project-file>.html.
- Camp Belge: legacy/campbelge.html. Its client is EDCL — Energy Development Corporation Limited.
- Kigali Ring: legacy/kigaliring.html. Its client is ELTEL Networks Sweden.
- Edit portfolio cards in project_list.html.
- Manage gallery photographs in Django admin > Project photos. All 20 projects are selectable. Set alternative text, order and active status there.
- Every legacy detail page includes partials/project_gallery.html. Empty galleries are hidden.
- Text is no longer read from apps/projects/catalog.py or the Project database table. Existing database records are preserved but are not registered in admin or used to override HTML.
- Project URL mappings live in apps/projects/legacy.py.
