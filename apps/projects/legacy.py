"""Mapping of clean project slugs to their original detail-page templates."""

PROJECT_TEMPLATES = {
    "keya-warehouse": "projects/legacy/keyawarehouse.html",
    "nyabarongo-substation": "projects/legacy/nyabarongosubstation.html",
    "kilinda-substation": "projects/legacy/kilindasubstation.html",
    "akagera-game-lodge": "projects/legacy/akageragamelodge.html",
    "epca-group-headquarters": "projects/legacy/epcaheadquater.html",
    "keya-nkora-cyimbili-hpp": "projects/legacy/hppworks.html",
    "kanombe-warehouses": "projects/legacy/kanombewarehouses.html",
    "karongi-quay": "projects/legacy/karongiquay.html",
    "lebanon-hotel": "projects/legacy/lebanonhotel.html",
    "luxury-apartments": "projects/legacy/luxury.html",
    "residential-house-kimihurura": "projects/legacy/residentialhouse.html",
    "rubavu-port": "projects/legacy/rubavuport.html",
    "rusizi-port": "projects/legacy/rusiziport.html",
    "shango-birembo-transmission": "projects/legacy/shangoproject.html",
    "trinity-school": "projects/legacy/trinityschool.html",
}

# Original file names used in legacy /allprojectsdetails.html/<file>.html URLs.
PROJECT_FILES = {v: k for k, v in {
    "keyawarehouse": "keya-warehouse",
    "kigaliring": "kigali-ring-transmission",
    "productiveusers": "productive-users",
    "epcwest": "epc-west",
    "campbelge": "camp-belge-transmission",
    "nyabarongosubstation": "nyabarongo-substation",
    "kilindasubstation": "kilinda-substation",
    "akageragamelodge": "akagera-game-lodge",
    "epcaheadquater": "epca-group-headquarters",
    "hppworks": "keya-nkora-cyimbili-hpp",
    "kanombewarehouses": "kanombe-warehouses",
    "karongiquay": "karongi-quay",
    "lebanonhotel": "lebanon-hotel",
    "luxury": "luxury-apartments",
    "residentialhouse": "residential-house-kimihurura",
    "rubavuport": "rubavu-port",
    "rusiziport": "rusizi-port",
    "shangoproject": "shango-birembo-transmission",
    "trinityschool": "trinity-school",
}.items()}