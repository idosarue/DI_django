from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')
    search_fields = ['name','email', 'phone_number']
   
admin.site.register(Person, PersonAdmin)