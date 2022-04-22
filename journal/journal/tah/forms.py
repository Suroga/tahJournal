from termios import FF1
from django import forms
from django.forms import formset_factory


class JournalForm(forms.Form):
    journal_name = forms.CharField(label='journal_name', max_length=100)
    meters = forms.CharField(label='meters', max_length=100)
    meters_corrections = forms.CharField(label='meters_corrections', max_length=100)

class StationForm(forms.Form):
    station_name = forms.CharField(label='station_name', max_length=100)
    station_height = forms.FloatField(label='station_height')
    sighting_points = forms.CharField(label='sighting_points', max_length=100)
    gorizontal_angle_gradus = forms.IntegerField(label='gorizontal_angle_gradus')
    gorizontal_angle_min = forms.FloatField(label='gorizontal_angle_min')
    sighting_points_neighbors = forms.IntegerField(label='sighting_points_neighbors')
    sighting_points_neighbors_height = forms.FloatField(label='sighting_points_neighbors_height')
    vertical_angle_gradus = forms.IntegerField(label='vertical_angle_gradus')
    vertical_angle_min = forms.FloatField(label='vertical_angle_min')
    rail = forms.FloatField(label='rail')
    # right_left = forms.CharField(label='f6', max_length=100)
    # right_left_neighbors = forms.CharField(label='f3', max_length=100)

StationFormset = formset_factory(StationForm, extra=1)
