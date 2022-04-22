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
    
    station_name = models.CharField(label='station_name', max_length=100)
    station_height = models.FloatField(label='station_height')
    sighting_points = models.CharField(label='sighting_points', max_length=100)
    gorizontal_angle_gradus = models.IntegerField(label='gorizontal_angle_gradus')
    gorizontal_angle_min = models.FloatField(label='gorizontal_angle_min')
    sighting_points_neighbors = models.IntegerField(label='sighting_points_neighbors')
    sighting_points_neighbors_height = models.FloatField(label='sighting_points_neighbors_height')
    vertical_angle_gradus = models.IntegerField(label='vertical_angle_gradus')
    vertical_angle_min = models.FloatField(label='vertical_angle_min')
    rail = models.FloatField(label='rail')    



# class JournalResults(models.Model):
#     # связь с Journal
#     pass