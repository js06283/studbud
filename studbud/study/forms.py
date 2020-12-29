from django import forms
from .models import Student
from django.forms import ModelForm
import pytz
from django.utils.safestring import mark_safe
from django.forms.widgets import RadioSelect

TIME_MANAGEMENT_CHOICES = [
    (1, 'Finish far before the deadline (days before the deadline)'),
    (2, 'Finish early (a day or two before the deadline)'),
    (3, 'Finish with a little bit of time left over (several hours before the deadline)'),
    (4, 'Finish at the last minute (several minutes before deadline)')
]
COLLABORATIVE_CHOICES = [
    (1, 'Prefer minimal talking'),
    (2, ''),
    (3, ''),
    (4, ''),
    (5, 'Very interactive')
]
SERIOUSNESS_CHOICES = [
    (1, 'Not so serious'),
    (2, ''),
    (3, ''),
    (4, ''),
    (5, 'Very serious student')
]
EXTROVERTED_CHOICES = [
    (1, 'Not extroverted'),
    (2, ''),
    (3, ''),
    (4, ''),
    (5, 'Very extroverted')
]
TIME_ZONE_CHOICES = [
    (1, 'UTC -4 through UTC -5 AKA Eastern (EST) or Central (CST)'),
    (2, 'UTC -6 through UTC -7 AKA Mountain (MST) or Pacific (PST)'),
    (3, 'UTC -8 through UTC -12 or UTC +12 through UTC +9'),
    (4, 'UTC +8 through UTC -3')
]
DISCOVERY_CHOICES = [
    ('class', 'Class'),
    ('discord', 'Discord'),
    ('facebook', 'Facebook'),
    ('friend', 'Friend'),
    ('groupme', 'GroupMe'),
    ('instagram', 'Instagram'),
    ('slack', 'Slack'),
    ('snapchat', 'Snapchat'),
    ('student_council', 'Student Council')
]

class StudentForm(ModelForm):
    first_name = forms.CharField(label= 'First Name ', widget=forms.TextInput)
    last_name = forms.CharField(label = 'Last Name ', widget=forms.TextInput)
    uni = forms.CharField(label = 'UNI ',widget=forms.TextInput)
    email = forms.CharField(label = 'Email ', widget=forms.TextInput)
    phone = forms.CharField(label = 'Phone number (optional)')
    time_zone = forms.ChoiceField(choices = TIME_ZONE_CHOICES, label = 'Time zone ')
    time_management = forms.ChoiceField(choices = TIME_MANAGEMENT_CHOICES, initial = 0, widget = forms.RadioSelect, label = 'How do you manage your time for assignments?')
    collaborative = forms.ChoiceField(choices = COLLABORATIVE_CHOICES, widget = forms.RadioSelect, label = 'How collaborative are you?')
    academic_seriousness = forms.ChoiceField(choices = SERIOUSNESS_CHOICES, widget = forms.RadioSelect, label = 'How serious of a student are you?')
    extroverted = forms.ChoiceField(choices = EXTROVERTED_CHOICES, widget = forms.RadioSelect, label = 'How extroverted are you?')
    discovery = forms.MultipleChoiceField(choices = DISCOVERY_CHOICES, widget = forms.CheckboxSelectMultiple)

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'uni', 'email', 'phone','time_zone', 'time_management',
                    'collaborative', 'academic_seriousness', 'extroverted', 'discovery']