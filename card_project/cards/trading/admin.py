from django.contrib import admin
from accounts.models import Profile
from .models import Card
# Register your models here.
admin.site.register(Profile)
admin.site.register(Card)
