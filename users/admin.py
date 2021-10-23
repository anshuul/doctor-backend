from django.contrib import admin
from .models import *
from django.forms import Form

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'sales_officer', 'category',
                    'is_qr_code_generated']

    def get_readonly_fields(self, request, obj=None):
        return ['qr_code']

    def is_qr_code_generated(self, obj):
        if obj.qr_code:
            return 'Yes'
        return 'No'
    is_qr_code_generated.short_description = 'Is QR CODE Generated ?'
    class Meta:
        model = Doctor

@admin.register(SalesOfficer)
class SalesOfficerAdmin(admin.ModelAdmin):
    list_display = ['name', 'region',]
    class Meta:
        model = SalesOfficer

@admin.register(SalesOfficerRegion)
class SalesOfficerRegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = SalesOfficerRegion

@admin.register(DoctorCategory)
class DoctorCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    class Meta:
        model = DoctorCategory