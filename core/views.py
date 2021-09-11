from django.forms.models import modelformset_factory
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import get_object_or_404, render

import core.models
from .models import User, Location, WorkEntry
from .forms import ReportForm, StempForm, StempFormSet
# Create your views here.
from django.forms import formset_factory

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


class reports_page(ListView):
    model = Location
    template_name = 'reports.html'
    form_class = ReportForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'workentries': WorkEntry.objects.all})
        return context


class stamps_page(CreateView): # CreateView, Model.FormSetFactory 10-15 instances (view = Calendar View third party package)
    model = WorkEntry
    template_name = 'stamps.html'
    form_class = StempForm
    #modelformset_factory = WorkEntry
    success_url = reverse_lazy('core:stamps')
    ArticleFormSet = formset_factory(StempForm)


class DoctorCreateView(CreateView):
    model = User
    template_name = 'create_user.html'
    fields = ['firstName', 'lastName', 'description','email', 'user']
    success_url = reverse_lazy('core:users')


def user_details(request, id):
    user = get_object_or_404(User, pk = int(id))
    return render(request , 'user_details.html', {'user':user})


class DoctorDetailsView(DetailView):
    model = User
    template_name = 'user_details.html'
    context_object_name = 'user'
