from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import User, Location
# Create your views here.


#@login_required
class admin_main(ListView):
    model = User
    template_name = 'main.html'   

class users_page(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

class locations_page(ListView):
    model = Location
    template_name = 'locations.html'

class reports_page(ListView):
    model = Location
    template_name = 'reports.html'

class stamps_page(ListView):
    model = Location
    template_name = 'stamps.html'

