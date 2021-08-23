from django.contrib import admin
from .models import Person
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')
    search_fields = ['name','email', 'phone_number']
    formfield_overrides = {
        models.CharField: {'widget': PhoneNumberInternationalFallbackWidget},
    }
admin.site.register(Person, PersonAdmin)