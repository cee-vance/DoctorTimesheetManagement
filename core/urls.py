from . import views
from django.urls import path
from core.views import admin_home

app_name ='core'

urlpatterns = [
    path('', admin_home.as_view(), name='admin_home'),
]