from django import forms
import datetime


CHOICES = {('TRUE', 'TRUE'),
           ('FALSE', 'FALSE')}

BIRTH_YEAR_CHOICE = ['1994', '1995']


"""


"""


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    date_field = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today)
    birth_year = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today)
    you_good = forms.ChoiceField(choices=CHOICES)



