from django import forms

class JournalForm(forms.Form):
    journal_name = forms.CharField(label='Jour name', max_length=100)
    param1 = forms.IntegerField(label='param1')

