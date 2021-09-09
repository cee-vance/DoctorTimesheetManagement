from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import User
# Create your views here.


#@login_required
class admin_home(ListView):
    model = User
    template_name = 'home.html'
    context_object_name = 'users'


"""
class CategoryDetail(generic.DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    
    
"""