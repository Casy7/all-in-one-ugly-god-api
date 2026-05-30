from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    last_recorded_photo = models.ImageField(upload_to='locations/', blank=True, null=True)

    def __str__(self):
        return self.name

class Army(models.Model):
    FACTION_CHOICES = [
        ('ORCS', 'Orcs'),
        ('ELVES', 'Elves'),
        ('DWARVES', 'Dwarves'),
        ('MEN', 'Men'),
        ('MONSTERS', 'Monsters'),
    ]
    name = models.CharField(max_length=255)
    faction = models.CharField(max_length=50, choices=FACTION_CHOICES)
    size = models.IntegerField(default=0)
    last_known_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='armies')
    last_recorded_photo = models.ImageField(upload_to='armies/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.faction})"

class Character(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=100)
    is_dangerous = models.BooleanField(default=True)
    last_known_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='characters')
    last_recorded_photo = models.ImageField(upload_to='characters/', blank=True, null=True)

    def __str__(self):
        return self.name