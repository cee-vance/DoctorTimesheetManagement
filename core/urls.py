from . import views
from django.urls import path, re_path
from core.views import admin_main, users_page, locations_page, reports_page, stamps_page ,\
    DoctorCreateView, DoctorDetailsView, CreateLocation,LocationUpdate , UserUpdate , LocationDelete,  \
    LocationDetail , UserDelete

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
    # update user
    path('<int:pk>/update_user/', UserUpdate.as_view(), name='update_user'),
    # delete user
    path('<int:pk>/delete_user/', UserDelete.as_view(), name='delete_user'),
    # location
    path('create_location/', CreateLocation.as_view(), name='create_location'),
    # update a location
    path('<int:pk>/update_location/', LocationUpdate.as_view(), name='update_location' ),


    #delete location
    path('<int:pk>/delete_location/' , LocationDelete.as_view(), name='delete_location'),
    #location detail
    path('<int:pk>/detail_location/', LocationDetail.as_view(), name = 'location_details')
]