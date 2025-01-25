from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from django.utils import timezone

# Testes para Models
class WalletModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test",email='test@teste.com', password='123456')
        

    def test_wallet_creation(self):
      
        self.assertEqual(self.wallet.balance, 100.0)

