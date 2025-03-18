from django.contrib import admin
from .models import student

# Register your models here.
@admin.register(student)
class studentadmin(admin.ModelAdmin):
   # list_display=("fname","lname","regno","register_date","email","branch")
    list_display=[ fields.name for fields in student._meta.get_fields()]
    
    
