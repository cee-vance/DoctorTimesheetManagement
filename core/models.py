from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class User( models.Model):
    user_id = IntegerField( null = False, on_delete=models.CASCADE)
    firstName = CharField( max_length=50, null= False)
    lastName = CharField( max_length=100, null= False)
    description = CharField(max_length=500 , null = True)
    # TO DO: change email field
    email = CharField( max_length = 100, null=True)
    login_id = CharField( max_length = 50, null = False)
    password = CharField( max_length = 50 , null = False)
    password_conf = CharField( max_length = 50, null = False)


class WorkEntry( models.Model):
    # Foreign key for User model
    doctor_id = ForeignKey(User, on_delete=models.CASCADE)
    date = DateTimeField(auto_null_add=True)
    start_time = IntegerField(null= True, default=0)
    end_time = IntegerField(null = True, default = 0)
    # To Do:

""""
TO DO:
lOCATION TABLE, HOURSCODE TABLE

"""



