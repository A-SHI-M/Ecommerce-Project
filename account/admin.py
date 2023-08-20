from django.contrib import admin
from account.models import Profile,User, CustomManager
# Register your models here.

admin.site.register(Profile)
admin.site.register(User)
