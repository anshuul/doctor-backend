from django.db import models

class SalesOfficerRegion(models.Model):
    name = models.CharField(max_length=50)

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
    
    def __str__(self):
        return self.name
