from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import JournalForm


def index(request):
    context = {
        'data': "SomeBody Tolds me"
        }
    return render(request, 'tah/index.html', context)

@login_required
def teor1(request):
    return render(request, 'teor/teor1.html')


def simplepocherk(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JournalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # print(form)
            # print(form.__attrs__)
            print(form.cleaned_data['journal_name'])
            print(form.cleaned_data['param1'])
            name = form.cleaned_data['journal_name']
            param1 = form.cleaned_data['param1']+1000
            # redirect to a new URL:
            return render(request, 'tah/results.html', {'name': name, 'param1': param1})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JournalForm()

    return render(request, 'tah/index.html', {'form': form})
    
    



