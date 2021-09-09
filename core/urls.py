from . import views
from django.urls import path, re_path


urlpatterns = [
    re_path('home/', views.admin_home, name='admin_home'),
]