from django import forms
from django.forms import fields
from core.models import User, Location, WorkEntry
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class ReportForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class StempForm(forms.ModelForm):
    class Meta:
        model = WorkEntry
        fields = '__all__'
