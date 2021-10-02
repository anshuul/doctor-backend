from django.db import models
from users.models import *

class ServiceLanguage(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=100)
    video_url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    categories = models.ForeignKey(DoctorCategory, on_delete=models.SET_NULL, null=True, blank=True)
    contents = models.ManyToManyField(Content)
    language = models.ForeignKey(ServiceLanguage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.categories.name
