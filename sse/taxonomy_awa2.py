"""Hand-written Order / Family / Genus for the 50 AwA2 classes.

Generic class names (e.g. "bat", "deer", "antelope") are mapped to a common
representative genus. Cetaceans use the traditional order "Cetacea".
"""

TAXONOMY = {
    # class name in AwA2      (order,           family,            genus)
    "antelope":          ("Artiodactyla",   "Bovidae",         "Antilope"),
    "grizzly+bear":      ("Carnivora",      "Ursidae",         "Ursus"),
    "killer+whale":      ("Cetacea",        "Delphinidae",     "Orcinus"),
    "beaver":            ("Rodentia",       "Castoridae",      "Castor"),
    "dalmatian":         ("Carnivora",      "Canidae",         "Canis"),
    "persian+cat":       ("Carnivora",      "Felidae",         "Felis"),
    "horse":             ("Perissodactyla", "Equidae",         "Equus"),
    "german+shepherd":   ("Carnivora",      "Canidae",         "Canis"),
    "blue+whale":        ("Cetacea",        "Balaenopteridae", "Balaenoptera"),
    "siamese+cat":       ("Carnivora",      "Felidae",         "Felis"),
    "skunk":             ("Carnivora",      "Mephitidae",      "Mephitis"),
    "mole":              ("Eulipotyphla",   "Talpidae",        "Talpa"),
    "tiger":             ("Carnivora",      "Felidae",         "Panthera"),
    "hippopotamus":      ("Artiodactyla",   "Hippopotamidae",  "Hippopotamus"),
    "leopard":           ("Carnivora",      "Felidae",         "Panthera"),
    "moose":             ("Artiodactyla",   "Cervidae",        "Alces"),
    "spider+monkey":     ("Primates",       "Atelidae",        "Ateles"),
    "humpback+whale":    ("Cetacea",        "Balaenopteridae", "Megaptera"),
    "elephant":          ("Proboscidea",    "Elephantidae",    "Loxodonta"),
    "gorilla":           ("Primates",       "Hominidae",       "Gorilla"),
    "ox":                ("Artiodactyla",   "Bovidae",         "Bos"),
    "fox":               ("Carnivora",      "Canidae",         "Vulpes"),
    "sheep":             ("Artiodactyla",   "Bovidae",         "Ovis"),
    "seal":              ("Carnivora",      "Phocidae",        "Phoca"),
    "chimpanzee":        ("Primates",       "Hominidae",       "Pan"),
    "hamster":           ("Rodentia",       "Cricetidae",      "Mesocricetus"),
    "squirrel":          ("Rodentia",       "Sciuridae",       "Sciurus"),
    "rhinoceros":        ("Perissodactyla", "Rhinocerotidae",  "Rhinoceros"),
    "rabbit":            ("Lagomorpha",     "Leporidae",       "Oryctolagus"),
    "bat":               ("Chiroptera",     "Vespertilionidae", "Myotis"),
    "giraffe":           ("Artiodactyla",   "Giraffidae",      "Giraffa"),
    "wolf":              ("Carnivora",      "Canidae",         "Canis"),
    "chihuahua":         ("Carnivora",      "Canidae",         "Canis"),
    "rat":               ("Rodentia",       "Muridae",         "Rattus"),
    "weasel":            ("Carnivora",      "Mustelidae",      "Mustela"),
    "otter":             ("Carnivora",      "Mustelidae",      "Lutra"),
    "buffalo":           ("Artiodactyla",   "Bovidae",         "Syncerus"),
    "zebra":             ("Perissodactyla", "Equidae",         "Equus"),
    "giant+panda":       ("Carnivora",      "Ursidae",         "Ailuropoda"),
    "deer":              ("Artiodactyla",   "Cervidae",        "Odocoileus"),
    "bobcat":            ("Carnivora",      "Felidae",         "Lynx"),
    "pig":               ("Artiodactyla",   "Suidae",          "Sus"),
    "lion":              ("Carnivora",      "Felidae",         "Panthera"),
    "mouse":             ("Rodentia",       "Muridae",         "Mus"),
    "polar+bear":        ("Carnivora",      "Ursidae",         "Ursus"),
    "collie":            ("Carnivora",      "Canidae",         "Canis"),
    "walrus":            ("Carnivora",      "Odobenidae",      "Odobenus"),
    "raccoon":           ("Carnivora",      "Procyonidae",     "Procyon"),
    "cow":               ("Artiodactyla",   "Bovidae",         "Bos"),
    "dolphin":           ("Cetacea",        "Delphinidae",     "Tursiops"),
}

LEVELS = ("order", "family", "genus")

# AwA2 predicate names that make up each facet.
HABITAT_PREDICATES = [
    "arctic", "coastal", "desert", "bush", "plains", "forest", "fields",
    "jungle", "mountains", "ocean", "ground", "water", "tree", "cave",
]
DIET_PREDICATES = ["fish", "meat", "plankton", "vegetation", "insects"]
