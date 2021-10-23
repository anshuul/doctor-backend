from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group

admin.site.site_header = admin.site.site_title = ("Zanpan's Admin Panel")
admin.site.index_title=('Admin')

admin.site.register(ServiceLanguage)
admin.site.register(Content)
# admin.site.register(Service)

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'service_contents', 'categories','selected_language']
    class Meta:
        model = Service
