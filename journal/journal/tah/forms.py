from termios import FF1
from django import forms
from django.forms import formset_factory


class JournalForm(forms.Form):
    journal_name = forms.CharField(label='Название журнала', max_length=100)
    meters = forms.CharField(label='Метры', max_length=100)
    meters_corrections = forms.CharField(label='Метры исправленные', max_length=100)

class StationForm(forms.Form):
    station_name = forms.CharField(label='station_name', max_length=100)
    station_height = forms.FloatField(label='station_height')
    sighting_points1 = forms.CharField(label='sighting_points1', max_length=100)
    sighting_points2 = forms.CharField(label='sighting_points2', max_length=100)
    sighting_points3 = forms.CharField(label='sighting_points3', max_length=100)
    sighting_points4 = forms.CharField(label='sighting_points4', max_length=100)
    gorizontal_angle_gradus1 = forms.IntegerField(label='gorizontal_angle_gradus1')
    gorizontal_angle_gradus2 = forms.IntegerField(label='gorizontal_angle_gradus2')
    gorizontal_angle_gradus3 = forms.IntegerField(label='gorizontal_angle_gradus3')
    gorizontal_angle_gradus4 = forms.IntegerField(label='gorizontal_angle_gradus4')
    gorizontal_angle_min1 = forms.FloatField(label='gorizontal_angle_min1')
    gorizontal_angle_min2 = forms.FloatField(label='gorizontal_angle_min2')
    gorizontal_angle_min3 = forms.FloatField(label='gorizontal_angle_min3')
    gorizontal_angle_min4 = forms.FloatField(label='gorizontal_angle_min4')
    sighting_points_neighbors1 = forms.CharField(label='sighting_points_neighbors1', max_length=100)
    sighting_points_neighbors2 = forms.CharField(label='sighting_points_neighbors2', max_length=100, required=False)
    sighting_points_neighbors_height1 = forms.CharField(label='sighting_points_neighbors_height1', max_length=100)
    sighting_points_neighbors_height2 = forms.CharField(label='sighting_points_neighbors_height2', max_length=100, required=False)
    vertical_angle_gradus1 = forms.CharField(label='vertical_angle_gradus1', max_length=100)
    vertical_angle_gradus2 = forms.CharField(label='vertical_angle_gradus2', max_length=100)
    vertical_angle_gradus3 = forms.CharField(label='vertical_angle_gradus3', max_length=100, required=False)
    vertical_angle_gradus4 = forms.CharField(label='vertical_angle_gradus4', max_length=100, required=False)
    vertical_angle_min1 = forms.CharField(label='vertical_angle_min1', max_length=100)
    vertical_angle_min2 = forms.CharField(label='vertical_angle_min2', max_length=100)
    vertical_angle_min3 = forms.CharField(label='vertical_angle_min3', max_length=100, required=False)
    vertical_angle_min4 = forms.CharField(label='vertical_angle_min4', max_length=100, required=False)
    rail1 = forms.CharField(label='rail1', max_length=100)
    rail2 = forms.CharField(label='rail2', max_length=100)
    rail3 = forms.CharField(label='rail3', max_length=100, required=False)
    rail4 = forms.CharField(label='rail4', max_length=100, required=False)
    #right_left = forms.CharField(label='right_or_left1', max_length=100)
    # right_left = forms.CharField(label='f6', max_length=100)
    # right_left_neighbors = forms.CharField(label='f3', max_length=100)
    # right_left = forms.CharField(label='f6', max_length=100)
    # right_left_neighbors = forms.CharField(label='f3', max_length=100)
    # right_left1 = forms.CharField(label='right_or_left1', max_length=100)
    # right_left2 = forms.CharField(label='right_or_left2', max_length=100)
    # right_left3 = forms.CharField(label='right_or_left3', max_length=100)
    # right_left4 = forms.CharField(label='right_or_left4', max_length=100)











StationFormset = formset_factory(StationForm, extra=1)
