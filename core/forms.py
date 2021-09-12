from django import forms
from django.db.models.fields import DateField
from django.forms import fields
from core.models import User, Location, WorkEntry
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory


class ReportForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'



class StempForm(forms.ModelForm):
    class Meta:
        model = WorkEntry
        fields = '__all__'
    
StempFormSet = modelformset_factory(WorkEntry, fields=('start_time', 'end_time'), extra=8,)


class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

