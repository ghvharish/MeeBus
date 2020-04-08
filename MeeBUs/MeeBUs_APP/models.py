from django.db import models

# Create your models here.
class PlaceName(models.Model):
    PlaceList=models.CharField(max_length=100)
    def __str__(self):
        return  self.PlaceList

class SourceSelect(models.Model):
    source=models.ForeignKey(PlaceName, on_delete=models.CASCADE)
    def __str__(self):
        return self.source

class DestinationSelect(models.Model):
    dest=models.ForeignKey(PlaceName, on_delete=models.CASCADE)
    def __str__(self):
        return self.dest