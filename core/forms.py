from django.forms import ModelForm
from .models import User


class DoctorCreateForm(ModelForm):
    class Meta:
        model = User
        fields = [ 'firstName', 'lastName', 'description', 'email']
