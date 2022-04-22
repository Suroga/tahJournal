from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import JournalForm, StationFormset, StationForm


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
        print(request.POST)
        print(request.POST)
        # raise Exception
        # create a form instance and populate it with data from the request:
        form1 = JournalForm(request.POST)
        form2 = StationFormset(request.POST)
        print(form1)
        print(form2)

        # check whether it's valid:
        if form1.is_valid() and form2.is_valid():
            satations = int(request.POST['form-TOTAL_FORMS'])

            #ИЛЬЯ, ДЕЛАЙ ТУТ
            print(form1.cleaned_data)
            for station in form2.cleaned_data:
                print(station)
            #ИЛЬЯ, ДЕЛАЙ ТУТ


            return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
        else:
            return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = JournalForm()
        form2 = StationFormset()

    return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
    
    



