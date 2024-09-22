from django.db import models

# Create your models here.
class Bank(models.Model):
    name = models.CharField(default="myBank", max_length=10)
    balance = models.DecimalField(default=0, max_digits=50, decimal_places=2) 
    def __str__(self) -> str:
        return self.name
    def update_balance(self, amount, transaction_type):
        if transaction_type == 'Deposit':
            self.balance += amount
        elif transaction_type == 'Withdrawal':
            self.balance -= amount
        self.save()