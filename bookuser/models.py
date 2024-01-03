from django.db import models
from bookuser.constants import GENDER_TYPE
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=100,choices = GENDER_TYPE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places = 2)
    birth_date = models.DateField()
    account_created_at = models.DateField(auto_now_add = True)


    def __str__(self) :
        return str(self.account_no)

class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_name = models.CharField(max_length=150)
    city = models.CharField(max_length = 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self) :
        return f'{self.user.first_name} {self.user.last_name}'