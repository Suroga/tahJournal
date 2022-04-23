from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import datetime
from .forms import JournalForm, StationFormset, StationForm
from .models import Journal, Station

def index(request):
    context = {
        'data': "SomeBody Tolds me"
        }
    return render(request, 'tah/index.html', context)

@login_required
def teor1(request):
    return render(request, 'teor/teor1.html')

@login_required
def calculation1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # raise Exception
        # create a form instance and populate it with data from the request:
        form1 = JournalForm(request.POST)
        form2 = StationFormset(request.POST)

        # check whether it's valid:
        if form1.is_valid() and form2.is_valid():
            stations = int(request.POST['form-TOTAL_FORMS'])

            #ИЛЬЯ, ДЕЛАЙ ТУТ
            j = Journal.objects.create(journal_name=form1.cleaned_data['journal_name'], meters=form1.cleaned_data['meters'], meters_corrections=form1.cleaned_data['meters_corrections'], date_of_creation=datetime.datetime.now())
            for station in form2.cleaned_data:
                Station.objects.create(journal=j,station_name = station['station_name'], station_height = station['station_height'], sighting_points = station['sighting_points'], gorizontal_angle_gradus = station['gorizontal_angle_gradus'], gorizontal_angle_min = station['gorizontal_angle_min'], sighting_points_neighbors = station['sighting_points_neighbors'], sighting_points_neighbors_height = station['sighting_points_neighbors_height'], vertical_angle_gradus = station['vertical_angle_gradus'], vertical_angle_min = station['vertical_angle_min'], rail = station['rail'])
            #ИЛЬЯ, ДЕЛАЙ ТУТ


            return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
        else:
            return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = JournalForm()
        form2 = StationFormset()

    return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
    
    



