from django.forms.models import inlineformset_factory, modelformset_factory
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect

import core.models
from .models import User, Location, WorkEntry
from .forms import ReportForm, StempForm,  LocationForm , DoctorCreateForm
# Create your views here.
from django.forms import formset_factory, inlineformset_factory

#@login_required
class admin_main(ListView):
    model = User
    template_name = 'main.html'   


class users_page(ListView):
    model = User
    #model = core.models.User
    template_name = 'users.html'
    context_object_name = 'users'


class locations_page(ListView):
    model = Location
    template_name = 'locations.html'
    context_object_name='locations'


class reports_page(ListView):
    model = Location
    template_name = 'reports.html'
    form_class = ReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'workentries': WorkEntry.objects.all})
        return context


def stamps_test_function(request):
    OrderFormSet = inlineformset_factory(User, WorkEntry, fields=('doctor_id', 'start_time', 'end_time', 'hourscode', 'location'))
    formset = OrderFormSet()
    #form = StempForm()
    context = {'formset': formset}
    if request.method == "POST":
        formset = OrderFormSet(request.POST)
        # form = StempForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    return render(request, 'stamps.html', context)



# USER / DOCTOR CRUD OPERATIONS

class DoctorCreateView(CreateView):
    """
    User / Doctor Create
    """
    model = User
    template_name = 'create_user.html'
    fields = ['firstName', 'lastName', 'description','email', 'user']
    success_url = reverse_lazy('core:users')

class UserDelete(DeleteView):
    """
    User/ Doctor Delete
    """
    model = User
    success_url = reverse_lazy('core:users')

class DoctorDetailsView(DetailView):
    """
    User/ Doctor details
    """
    model = User
    template_name = 'user_details.html'
    context_object_name = 'user'

class UserUpdate(UpdateView):
    """
    Update a User
    """
    model = User
    form_class = DoctorCreateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('core:users')



# LOCATION CRUD OPERATIONS

class CreateLocation(CreateView):
    """
    Create a location to be used
    by a workentry item
    """
    model = Location
    template_name = 'create_location.html'
    fields = '__all__'
    success_url = reverse_lazy('core:locations')

class LocationUpdate(UpdateView):
    """
    Update a Location
    """
    model = Location
    form_class = LocationForm
    template_name = 'update_location.html'
    success_url = reverse_lazy('core:locations')



class LocationDelete(DeleteView):
    """
    Delete a location
    """
    model = Location

    success_url = reverse_lazy('core:locations')

class LocationDetail(DetailView):
    """
    Shows details of location
    """
    model = Location
    template_name = 'location_details.html'
    context_object_name = 'location'