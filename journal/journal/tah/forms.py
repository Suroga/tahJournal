from termios import FF1
from django import forms
from django.forms import formset_factory


class JournalForm(forms.Form):
    journal_name = forms.CharField(label='Jour name', max_length=100)

class CalculationForm(forms.Form):
    f1 = forms.CharField(label='f1', max_length=100)
    f2 = forms.CharField(label='f2', max_length=100)
    f3 = forms.CharField(label='f3', max_length=100)
    f4 = forms.CharField(label='f4', max_length=100)
    f5 = forms.CharField(label='f5', max_length=100)
    f6 = forms.CharField(label='f6', max_length=100)
    f7 = forms.CharField(label='f7', max_length=100)

CalculationFormset = formset_factory(CalculationForm, extra=100)
