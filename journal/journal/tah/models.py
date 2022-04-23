from django.db import models

class Journal(models.Model):
    """Model representing an author."""
    journal_name = models.CharField(null=False, blank=False, max_length=100)
    meters = models.CharField(null=False, blank=False, max_length=100)
    meters_corrections = models.CharField(null=False, blank=False, max_length=100)
    date_of_creation = models.DateField('Created', null=True, blank=True)


class Station(models.Model):
    # связь с journal
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    
    station_name = models.CharField(max_length=100)
    station_height = models.FloatField()
    sighting_points = models.CharField( max_length=100)
    gorizontal_angle_gradus = models.IntegerField()
    gorizontal_angle_min = models.FloatField()
    sighting_points_neighbors = models.IntegerField()
    sighting_points_neighbors_height = models.FloatField()
    vertical_angle_gradus = models.IntegerField()
    vertical_angle_min = models.FloatField()
    rail = models.FloatField()    



# class JournalResults(models.Model):
#     # связь с Journal
#     pass