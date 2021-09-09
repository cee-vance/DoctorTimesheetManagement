from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import User
# Create your views here.


#@login_required
class admin_home(ListView):
    model = User
    template_name = 'home.html'
    

class users_page(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

