from django.db import models
from bookuser.models import UserAccount

# Create your models here.
class Transaction(models.Model):
    account = models.ForeignKey(UserAccount, on_delete = models.CASCADE, related_name = 'accounts')
    amount = models.DecimalField(max_digits = 12, decimal_places = 2)
    timestamp = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['timestamp']