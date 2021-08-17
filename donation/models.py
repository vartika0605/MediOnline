from django.contrib.gis.db import models
from django.contrib.auth.models import User
class NeedPlasma(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    # For the location, you are using the PointField, a GeoDjango-specific geometric field for storing a GEOS Point object that represents a pair of longitude and latitude coordinates.
    location = models.PointField()
    person_id = models.AutoField
    person_email = models.CharField(max_length=50,default="")
  
    file_field = models.FileField(upload_to='needPlasma/')
    person_mobileNumber =  models.CharField(max_length=12,default="")
    person_age =models.IntegerField(default=0)
    person_address= models.CharField(max_length=200)
    
   
    person_gender= models.CharField(max_length=20)
    
    



class DonatePlasma(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100)
    # For the location, you are using the PointField, a GeoDjango-specific geometric field for storing a GEOS Point object that represents a pair of longitude and latitude coordinates.
    location = models.PointField()
    person_id = models.AutoField
    person_email = models.CharField(max_length=50,default="")
  
    
    person_mobileNumber = models.CharField(max_length=12,default="")
    person_age =models.IntegerField(default=0)
   
    person_address= models.CharField(max_length=200)
    
    date_last_tested_negative = models.DateField(
        "Date Last Tested Negative for COVID19 ", blank=False)
    last_covid_report = models.FileField(upload_to='donatePlasma/')

    igg_report = models.FileField(upload_to='donatePlasma/')