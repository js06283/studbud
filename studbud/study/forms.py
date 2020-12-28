from django import forms
from .models import Student
from django.forms import ModelForm
import pytz

class StudentForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)
    uni = forms.CharField(widget=forms.TextInput)
    email = forms.CharField(widget=forms.TextInput)
    time_zone = forms.ChoiceField(choices=[(tz, tz) for tz in pytz.all_timezones])

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'uni', 'email']