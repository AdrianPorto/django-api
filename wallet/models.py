from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} - Saldo: {self.balance}"

class Transaction(models.Model):
    sender = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"De {self.sender.username} para {self.recipient.username} - {self.amount}"                                                                                                                          