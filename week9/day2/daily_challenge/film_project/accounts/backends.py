from django.contrib.auth.backends import BaseBackend, ModelBackend
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from .models import NewUser

# class MyModelBackend(BaseBackend):
#     def authenticate(self, request, email=None, password=None, **kwarhgs):
#         print('hey form models authe')       # user = get_object_or_404(NewUser, email=email)
#         try:
#             user = NewUser.objects.get(email=email)
#         except NewUser.DoesNotExist:
#             print('error does not exist')
#             return
#         if user.check_password(password):
#             return user
#         else:
#             print('error password')
#             return 


class MyModelBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        NewUser = get_user_model()
        if email is None:
            email = kwargs.get(NewUser.USERNAME_FIELD)
        try:
            case_insetsitive_username_field = '{}__iexact'.format(NewUser.USERNAME_FIELD)
            user = NewUser._default_manager.get(**{case_insetsitive_username_field: email})
        except NewUser.DoesNotExist:
            print('error does not exist')
            NewUser.set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            # print('error password')
            # return 