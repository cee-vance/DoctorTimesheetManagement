from . import views
from django.urls import path
from core.views import admin_main, users_page, locations_page, reports_page, stamps_page

app_name ='core'

urlpatterns = [
    path('', admin_main.as_view(), name='admin_main'),
    path('users/', users_page.as_view() , name='users'),
    path('locations/', locations_page.as_view() , name='locations'),
    path('stamps/', stamps_page.as_view() , name='stamps'),
    path('reports/', reports_page.as_view() , name='reports')
]