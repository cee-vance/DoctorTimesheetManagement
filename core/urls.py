from . import views
from django.urls import path
from core.views import admin_home

app_name ='core'

urlpatterns = [
<<<<<<< HEAD
    path('', admin_home.as_view(), name='admin_home'),
=======
    re_path('home/', views.admin_home, name='admin_home'),
>>>>>>> 4f27825e94fd784260fd40ac5fc8a84e685afff9
]