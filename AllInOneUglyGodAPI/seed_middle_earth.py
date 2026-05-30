import os
import django
import random

# setup django environment before importing models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AllInOneUglyGodAPI.settings')
django.setup()

from PalInTears.models import Location, Army, Character

def seed_data():
    print("Clearing old middle-earth records...")
    Character.objects.all().delete()
    Army.objects.all().delete()
    Location.objects.all().delete()

    print("Generating locations...")
    loc_names = ["Mordor", "Rivendell", "The Shire", "Gondor", "Rohan", "Erebor", "Lothlorien", "Isengard", "Moria", "Mirkwood"]
    locations = []
    for name in loc_names:
        loc = Location.objects.create(name=name, description=f"Strategic region known as {name}")
        locations.append(loc)

    print("Generating armies...")
    army_data = [
        ("Uruk-hai Vanguard", "ORCS", 15000),
        ("Gorgoroth Iron Garrison", "ORCS", 40000),
        ("Lothlorien Border Guards", "ELVES", 3000),
        ("Rivendell Rivendell Horsemen", "ELVES", 1200),
        ("Erebor Shield-wall", "DWARVES", 5000),
        ("Iron Hills Veterans", "DWARVES", 4500),
        ("Riders of the Riddermark", "MEN", 6000),
        ("Gondor Citadel Guard", "MEN", 8000),
        ("Shelob's Brood", "MONSTERS", 150),
        ("Misty Mountain Goblins", "ORCS", 12000)
    ]
    for name, faction, size in army_data:
        Army.objects.create(
            name=name,
            faction=faction,
            size=size,
            last_known_location=random.choice(locations)
        )

    print("Generating personal entities...")
    char_data = [
        ("Gandalf the Grey", "Maia", False),
        ("Sauron", "Maia", True),
        ("Aragorn", "Man", False),
        ("Legolas Greenleaf", "Elf", False),
        ("Gimli son of Gloin", "Dwarf", False),
        ("Frodo Baggins", "Hobbit", False),
        ("Saruman the White", "Maia", True),
        ("Witch-king of Angmar", "Wraith", True),
        ("Galadriel", "Elf", False),
        ("Gollum", "Stoor Hobbit", True)
    ]
    for name, race, dangerous in char_data:
        Character.objects.create(
            name=name,
            race=race,
            is_dangerous=dangerous,
            last_known_location=random.choice(locations)
        )

    print("Middle-earth synchronization complete. 30 targets loaded into PalInTears.")

if __name__ == '__main__':
    seed_data()