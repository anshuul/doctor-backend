from django.db import models
from django.db.models.signals import post_save
from .signals import post_save_activities_for_doctor

class SalesOfficerRegion(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class SalesOfficer(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(SalesOfficerRegion, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.region}'

class DoctorCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    sales_officer = models.ForeignKey(SalesOfficer,on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(DoctorCategory, on_delete=models.SET_NULL, null=True, blank=True, )
    qr_code = models.ImageField(upload_to='media/qr_codes', null=True, blank=True)
    
    def __str__(self):
        return self.name

post_save.connect(post_save_activities_for_doctor, sender=Doctor)
