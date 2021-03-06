from django.forms.models import inlineformset_factory, modelformset_factory
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect,HttpResponse


import core.models
from .models import User, Location, WorkEntry
from .forms import ReportForm, StempForm,  LocationForm , DoctorCreateForm, StepFormSet 
# Create your views here.
from django.forms import formset_factory, inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from .filters import WorkEntryFilter


class admin_main(ListView):
    model = User
    template_name = 'main.html'   



class users_page(UserPassesTestMixin, ListView):
    model = User
    #model = core.models.User
    template_name = 'users.html'
    context_object_name = 'users'
    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()


class locations_page(ListView):
    model = Location
    template_name = 'locations.html'
    context_object_name='locations'




class stamps_page(ListView):
    model = WorkEntry
    template_name = 'stamps.html'
    form_class = StempForm
    context_object_name='stamps'

    # def test_func(self):
    #     return self.request.user.groups.filter(name='admin').exists()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'user_key': User.objects.all})
        return context

def stamps_second_test_function(request, pk):
    user = User.objects.get(pk=pk)
    formset = StepFormSet(request.POST or None)

    if request.method == "POST":
        if formset.is_valid():
            formset.instance = user
            formset.save()
            return HttpResponseRedirect('/core/')
    context = {
        "formset": formset,
        "user": user
    }
    return render(request, 'stamps_detail.html', context)



# USER / DOCTOR CRUD OPERATIONS

class DoctorCreateView(UserPassesTestMixin,CreateView):
    """
    User / Doctor Create
    """
    model = User
    template_name = 'create_user.html'
    fields = ['firstName', 'lastName', 'description','email', 'user']
    success_url = reverse_lazy('core:users') # 2 forms / new fiels is admin 

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

class UserDelete(UserPassesTestMixin, DeleteView):
    """
    User/ Doctor Delete
    """
    model = User
    success_url = reverse_lazy('core:users')

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

class DoctorDetailsView(UserPassesTestMixin,DetailView):
    """
    User/ Doctor details
    """
    model = User
    template_name = 'user_details.html'
    context_object_name = 'user'

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

class UserUpdate(UserPassesTestMixin, UpdateView):
    """
    Update a User
    """
    model = User
    form_class = DoctorCreateForm
    template_name = 'update_user.html'
    success_url = reverse_lazy('core:users')

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()



# LOCATION CRUD OPERATIONS

class CreateLocation( UserPassesTestMixin, CreateView):
    """
    Create a location to be used
    by a workentry item
    """
    model = Location
    template_name = 'create_location.html'
    fields = '__all__'
    success_url = reverse_lazy('core:locations')

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

class LocationUpdate(UserPassesTestMixin, UpdateView):
    """
    Update a Location
    """
    model = Location
    form_class = LocationForm
    template_name = 'update_location.html'
    success_url = reverse_lazy('core:locations')

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()



class LocationDelete(UserPassesTestMixin, DeleteView):
    """
    Delete a location
    """
    model = Location
    success_url = reverse_lazy('core:locations')

    def test_func(self):
        return self.request.user.groups.filter(name='admin').exists()

class LocationDetail(DetailView):
    """
    Shows details of location
    """
    model = Location
    template_name = 'location_details.html'
    context_object_name = 'location'


def reports_page(request):
    """"
    Filters WorkEntry items by user, date , location, and hourscode
    """
    # if not request.user.groups.filter(name='admin').exists():
    #     return HttpResponse('Must be admin to view reports page')
    entries = WorkEntry.objects.all()

    filter = WorkEntryFilter(request.GET, queryset=entries)
    entries = filter.qs
    context = {
        'entries': entries,
        'filter': filter
    }
    return render(request, 'reports.html', context)
