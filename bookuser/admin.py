from django.contrib import admin
from bookuser.models import UserAccount, UserAddress

# Register your models here.
admin.site.register(UserAccount)
admin.site.register(UserAddress)