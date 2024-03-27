from django.db import models
from django.contrib.auth import get_user_model

class Client(models.Model):
    bank_account_number = models.CharField(max_length = 20)
    mobile_number = models.CharField(max_length = 11)

    def __str__(self):
        return self.mobile_number

class Transaction(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    timestap = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.client.mobile_number} - {self.amount}"


