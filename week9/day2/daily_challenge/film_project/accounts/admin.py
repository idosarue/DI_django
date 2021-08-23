
from django.contrib import admin
from .models import NewUser

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    class Meta:
        model = NewUser
admin.site.register(NewUser, UserAdmin)
# Register your models here.
