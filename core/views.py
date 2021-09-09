from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
# Create your views here.


#@login_required
class admin_home(ListView):
    model = User
    template = 'home.html'
    context_object_name = 'users'
