from . import views
from django.urls import path
from core.views import admin_home, users_page

app_name ='core'

urlpatterns = [
    path('', admin_home.as_view(), name='admin_home'),
    path('users/', users_page.as_view() , name='users')
]