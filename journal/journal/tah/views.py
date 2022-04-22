from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import JournalForm, CalculationForm, CalculationFormset


def index(request):
    context = {
        'data': "SomeBody Tolds me"
        }
    return render(request, 'tah/index.html', context)

@login_required
def teor1(request):
    return render(request, 'teor/teor1.html')

@login_required
def simplepocherk(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = JournalForm(request.POST)
        form2 = CalculationFormset(request.POST)
        # check whether it's valid:
        if form1.is_valid():
            # process the data in form1.cleaned_data as required
            # print(form1)
            # print(form1.__attrs__)
            print(form1.cleaned_data['journal_name'])
            print(form1.cleaned_data['param1'])
            name = form1.cleaned_data['journal_name']
            param1 = form1.cleaned_data['param1']
            # redirect to a new URL:
            return render(request, 'tah/results.html', {'name': name, 'param1': param1})

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = JournalForm()
        form2 = CalculationFormset()

    return render(request, 'tah/calculation1.html', {'form1': form1, 'form2': form2})
    
    



