from django.db.models import Model, CharField, FloatField


class Location(Model):
    """
    Model for managing locations
    """
    name = CharField(max_length=200, unique=True)
    lat = FloatField(unique=True)
    long = FloatField(unique=True)

    class Meta:
        unique_together = ['name', 'lat', 'long']