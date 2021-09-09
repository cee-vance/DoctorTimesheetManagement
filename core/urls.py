from . import views
from django.urls import path, re_path


urlpatterns = [
    re_path('home/', views.home, name='admin_home'),
]