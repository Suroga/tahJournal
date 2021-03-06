from django.db import models
from journal.users.models import User

class Journal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """Model representing an author."""
    journal_name = models.CharField(null=False, blank=False, max_length=100)
    meters = models.CharField(null=False, blank=False, max_length=100)
    meters_corrections = models.CharField(null=False, blank=False, max_length=100)
    date_of_creation = models.DateField('Created', null=True, blank=True)


class Station(models.Model):
    # связь с journal
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    
    #TODO

    # station_name 
    # station_height
    # sighting_points1
    # sighting_points2
    # sighting_points3
    # sighting_points4
    # gorizontal_angle_gradus1
    # gorizontal_angle_gradus2
    # gorizontal_angle_gradus3
    # gorizontal_angle_gradus4
    # gorizontal_angle_min1
    # gorizontal_angle_min2
    # gorizontal_angle_min3
    # gorizontal_angle_min4
    # sighting_points_neighbors1
    # sighting_points_neighbors2
    # sighting_points_neighbors_height1
    # sighting_points_neighbors_height2
    # vertical_angle_gradus1
    # vertical_angle_gradus2
    # vertical_angle_gradus3
    # vertical_angle_gradus4
    # vertical_angle_min1
    # vertical_angle_min2
    # vertical_angle_min3
    # vertical_angle_min4
    # rail1
    # rail2
    # rail3
    # rail4

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