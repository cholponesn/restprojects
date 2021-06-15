from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','full_name','photo','count_order','wallet','sale']

admin.site.register(Profile,ProfileAdmin)
