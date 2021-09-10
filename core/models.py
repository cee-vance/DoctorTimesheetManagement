from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    """"
    The user of the Doctor Management System
    usually a doctor
    """
    firstName = models.CharField( max_length=50, null= False)
    lastName = models.CharField( max_length=100, null= False)
    description = models.CharField(max_length=500 , null = True)
    # TO DO: change email field
    email = models.EmailField( max_length = 254, null=True)

    user = models.ForeignKey(User, on_delete = CASCADE, default = 1 )
    email_conf = models.BooleanField(default = False)



class HoursCode(models.Model): # no DB
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
    SECTOR_CHOICES = (('E', 'East'), ('W', 'West'))
    name = models.CharField(max_length=50, null= False)
    sector = models.CharField(choices = SECTOR_CHOICES, max_length = 4,default = 'East')
    address = models.CharField(max_length=150, null=True)

class WorkEntry( models.Model):
    """
    Represents a doctors work entry
    including date , start, end time,
    hours code for billing and a reference
    to the doctor who worked
    """
    HC_CHOICES = (('A', 'AMCO'), ('F', 'FPB'))
    doctor_id = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    start_time = models.IntegerField(null= True, default=0)
    end_time = models.IntegerField(null = True, default = 0)
    hourscode = models.CharField(choices = HC_CHOICES, max_length = 4, default = 'AMCO')



