from re import U
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from .forms import JournalForm, StationFormset, StationForm
from .models import Journal, Station
from journal.users.models import User
from .calculations import calculations 


# @login_required
def calculation1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # raise Exception
        # create a form instance and populate it with data from the request:
        form1 = JournalForm(request.POST)
        form2 = StationFormset(request.POST)

        # check whether it's valid:
        if form1.is_valid() and form2.is_valid():
            print(form1.cleaned_data['journal_name'])
            stations = int(request.POST['form-TOTAL_FORMS'])

            username = request.user.username
            u = User.objects.get(username=username)
            #ИЛЬЯ, ДЕЛАЙ ТУТ
            j = Journal.objects.create(journal_name=form1.cleaned_data['journal_name'], meters=form1.cleaned_data['meters'], meters_corrections=form1.cleaned_data['meters_corrections'], date_of_creation=datetime.datetime.now(), user=u)
            for station in form2.cleaned_data:
                Station.objects.create(journal=j,
                    station_name=station['station_name'],
                    station_height=station['station_height'],
                    sighting_points1=station['sighting_points1'],
                    sighting_points2=station['sighting_points2'],
                    sighting_points3=station['sighting_points3'],
                    sighting_points4=station['sighting_points4'],
                    gorizontal_angle_gradus1=station['gorizontal_angle_gradus1'],
                    gorizontal_angle_gradus2=station['gorizontal_angle_gradus2'],
                    gorizontal_angle_gradus3=station['gorizontal_angle_gradus3'],
                    gorizontal_angle_gradus4=station['gorizontal_angle_gradus4'],
                    gorizontal_angle_min1=station['gorizontal_angle_min1'],
                    gorizontal_angle_min2=station['gorizontal_angle_min2'],
                    gorizontal_angle_min3=station['gorizontal_angle_min3'],
                    gorizontal_angle_min4=station['gorizontal_angle_min4'],
                    sighting_points_neighbors1=station['sighting_points_neighbors1'],
                    sighting_points_neighbors2=station['sighting_points_neighbors2'],
                    sighting_points_neighbors_height1=station['sighting_points_neighbors_height1'],
                    sighting_points_neighbors_height2=station['sighting_points_neighbors_height2'],
                    vertical_angle_gradus1=station['vertical_angle_gradus1'],
                    vertical_angle_gradus2=station['vertical_angle_gradus2'],
                    vertical_angle_gradus3=station['vertical_angle_gradus3'],
                    vertical_angle_gradus4=station['vertical_angle_gradus4'],
                    vertical_angle_min1=station['vertical_angle_min1'],
                    vertical_angle_min2=station['vertical_angle_min2'],
                    vertical_angle_min3=station['vertical_angle_min3'],
                    vertical_angle_min4=station['vertical_angle_min4'],
                    rail1=station['rail1'],
                    rail2=station['rail2'],
                    rail3=station['rail3'],
                    rail4=station['rail4'],                                    
                    )
            #ИЛЬЯ, ДЕЛАЙ ТУТ
            calculations()            
            return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
        else:
            return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
    else:
        form1 = JournalForm()
        form2 = StationFormset()

    return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})


def teor(request, id):
    teorId = id
    return render(request, f'teor/teor{teorId}.html')


def index(request):
    if request.method == 'POST':
        pass
    else:
        pass
    
    



