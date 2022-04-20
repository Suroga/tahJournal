from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    context = {
        'data': "SomeBody Tolds me"
        }
    return render(request, 'tah/index.html', context)