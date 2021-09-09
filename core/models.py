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



class HoursCode(models.Model):
    """
    Defines the type of hours worked
    choices are AMCO or FPB
    """
    CHOICES = (('A','AMCO'), ('F','FPB'))
    code = models.CharField(choices = CHOICES, max_length=4, default = 'A')


class Sector(models.Model):
    """
    Divides all the locations into sectors
    choices are east and west
    """
    SectorChoices =  (('E','East'), ('W','West'))

    name = models.CharField(choices = SectorChoices, max_length=4 )


class Location(models.Model):
    """
    Represents the physical location
    where a WorkEntry took place
    """
    name = models.CharField(max_length=50, null= False)
    sector_id = models.ForeignKey(Sector, on_delete=CASCADE)
    address = models.CharField(max_length=150, null=True)

class WorkEntry( models.Model):
    # Foreign key for User model
    doctor_id = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.IntegerField(null= True, default=0)
    end_time = models.IntegerField(null = True, default = 0)
    hourscode_id = models.ForeignKey(HoursCode, on_delete=CASCADE, default=0)

    # To Do:

""""
TO DO:
lOCATION TABLE, HOURSCODE TABLE

"""

