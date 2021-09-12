from . import views
from django.urls import path, re_path
from core.views import admin_main, users_page, locations_page, reports_page, stamps_page ,\
    DoctorCreateView, DoctorDetailsView, CreateLocation,LocationUpdate , UserUpdate , LocationDelete

app_name ='core'

urlpatterns = [
    path('', admin_main.as_view(), name='admin_main'),
    path('users/', users_page.as_view() , name='users'),
    path('locations/', locations_page.as_view() , name='locations'),
    path('stamps/', stamps_page.as_view() , name='stamps'),
    path('reports/', reports_page.as_view() , name='reports'),
    # create a doctor / user
    path('create_user/', DoctorCreateView.as_view(), name='create_user'),
    # doctor / user details ... link from users.html
    path('<int:pk>/detail_user/',DoctorDetailsView.as_view() , name='user_details'),

    path('create_location/', CreateLocation.as_view(), name='create_location'),
    # update a location
    path('update_location/<int:pk>/', LocationUpdate.as_view(), name='update_location' ),
    #update user
    path('update_user/<int:pk>/', UserUpdate.as_view(), name='update_user' ),

    #delete location
    path('delete_location/<int:pk>/' , LocationDelete.as_view(), name='delete_location'),
]