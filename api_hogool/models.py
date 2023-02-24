from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class FarmerInfo(models.Model):
    farmer_id=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(default=" ", blank=False, null=False, max_length=35)
    phone=models.CharField(max_length=15,blank=False,null=False)
    description=models.TextField(max_length=500,blank=True,null=True)
    experince=models.IntegerField(default=0,blank=False,null=False)
    profile_photo=models.CharField(max_length=500,blank=True,null=True)
    location=models.CharField(max_length=15,default='الخرطوم',blank=False,null=False)
    avalability_for_job=models.BooleanField(default=False,blank=False,null=False)

class InvestorInfo(models.Model):
    investor_id = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    full_name = models.CharField(default=" ", blank=False, null=False, max_length=35)
    phone = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    profile_photo = models.CharField(max_length=500,blank=True, null=True)
    location = models.CharField(max_length=15,default='الخرطوم', blank=False, null=False)

class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name=models.CharField(blank=False,null=False,max_length=35)
    account_type=models.CharField(blank=False,null=False,max_length=10)
    account_avalability=models.BooleanField(default=False, blank=False, null=False)

class News(models.Model):
    title = models.CharField(max_length=100,blank=False, null=False)
    pic=models.CharField(max_length=500,blank=True, null=True)
    contnet=models.TextField(max_length=1000,blank=False, null=False)
    avalability=models.BooleanField(default=True,blank=False, null=False)

class Crops(models.Model):
    crop = models.CharField(blank=False, null=False, max_length=15)

class FarmerCrops(models.Model):
    Farmer=models.ForeignKey(User,on_delete=models.CASCADE)
    crop=models.ForeignKey(Crops,on_delete=models.CASCADE)

class land(models.Model):
    land_oner=models.ForeignKey(User,on_delete=models.CASCADE)
    space=models.IntegerField(blank=False,null=False)
    title = models.TextField(default=" ", blank=False, null=False, max_length=30)
    duration=models.IntegerField(default=6,blank=False,null=False)
    description=models.TextField(max_length=500,blank=False,null=False)
    price_rent=models.IntegerField(blank=False,null=False)
    Location=models.CharField(max_length=15,default='الخرطوم',null=False,blank=False)
    irrigation_typemodels=models.CharField(max_length=15,null=False,blank=False)
    avalability=models.BooleanField()

class InvestmentOffers(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    financing=models.IntegerField(blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    title = models.TextField(default=" ", blank=False, null=False, max_length=30)
    location=models.CharField(max_length=15,default='الخرطوم',null=False,blank=False)
    duration=models.IntegerField(default=6,blank=False,null=False)
    space = models.IntegerField(blank=False, null=False)
    description_the_land=models.TextField(max_length=500,blank=False,null=False)
    irrigation_typemodels = models.CharField(max_length=500,null=False, blank=False)
    avalability = models.BooleanField(default=False)

class OrderJob(models.Model):
    creater=models.ForeignKey(User,on_delete=models.CASCADE,related_name='creater')
    investor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='investor')
    farmer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='farmer')
    invesment_offer=models.ForeignKey(InvestmentOffers,on_delete=models.CASCADE)
    state=models.CharField(max_length=15,blank=False,null=False,default='معلق')

class FarmerProject(models.Model):
    farmer=models.ForeignKey(User,on_delete=models.CASCADE,related_name='farmer1')
    creater=models.ForeignKey(User,on_delete=models.CASCADE,related_name='creater1')
    investor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='investor1')
    invesment_offer = models.ForeignKey(InvestmentOffers, on_delete=models.CASCADE)
    state = models.CharField(max_length=15,blank=False, null=False, default='معلق')

class OrerdLandRent(models.Model):
    land=models.ForeignKey(land,on_delete=models.CASCADE)
    user_request=models.ForeignKey(User,on_delete=models.CASCADE,related_name='requestrer')
    land_owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='onerLand')
    state = models.CharField(max_length=15,blank=False, null=False, default='معلق')
