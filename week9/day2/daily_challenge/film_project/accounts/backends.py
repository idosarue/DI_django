from django.contrib.auth.backends import BaseBackend
from django.shortcuts import get_object_or_404
from .models import NewUser

class MyModelBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        print('hey form models authe')       # user = get_object_or_404(NewUser, email=email)
        try:
            user = NewUser.objects.get(email=email)
        except NewUser.DoesNotExist:
            print('error does not exist')
            return
        if user.check_password(password):
            return user
        else:
            print('error password')
            return 