from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField( null = False)
    firstName = models.CharField( max_length=50, null= False)
    lastName = models.CharField( max_length=100, null= False)
    description = models.CharField(max_length=500 , null = True)
    # TO DO: change email field
    email = models.CharField( max_length = 100, null=True)
    login_id = models.CharField( max_length = 50, null = False)
    password = models.CharField( max_length = 50 , null = False)
    password_conf = models.CharField( max_length = 50, null = False)


class WorkEntry( models.Model):
    # Foreign key for User model
    doctor_id = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.IntegerField(null= True, default=0)
    end_time = models.IntegerField(null = True, default = 0)
    # To Do:

""""
TO DO:
lOCATION TABLE, HOURSCODE TABLE

"""



