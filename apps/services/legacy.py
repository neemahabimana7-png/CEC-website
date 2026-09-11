"""Mapping of clean service slugs to their original detail-page templates."""

SERVICE_TEMPLATES = {
    "power-transmission": "services/legacy/powertransmission.html",
    "civil-structural": "services/legacy/civil&engineering.html",
    "building": "services/legacy/building.html",
    "mep": "services/legacy/mep.html",
    "marine": "services/legacy/marine.html",
    "water": "services/legacy/water.html",
}

# Original file names used by marine.js to identify each service page.
SERVICE_FILES = {
    "power-transmission": "powertransmission.html",
    "civil-structural": "civil&engineering.html",
    "building": "building.html",
    "mep": "MPEP.html",
    "marine": "marine.html",
    "water": "water.html",
}