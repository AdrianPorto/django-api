from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from wallet.models import Wallet, Transaction
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios para demonstração'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populando o banco de dados...')

        # Criar usuários
        users = []
        for i in range(1, 6):
            user = User.objects.create_user(username=f'user{i}', email=f'user{i}@email.com', password='123456')
            users.append(user)
            self.stdout.write(f'Usuário {user.username} criado.')

        # Criar carteiras
        wallets = []
        for user in users:
            wallet = user.wallet
            wallet.balance = random.uniform(100.0, 1000.0)
            wallet.save()
            wallets.append(wallet)
            self.stdout.write(f'Carteira para {user.username} criada com saldo {wallet.balance:.2f}.')

        # Criar transaçõescl
        for i in range(10):
            sender = random.choice(wallets)
            recipient = random.choice([w for w in wallets if w != sender])
            amount = round(random.uniform(10.0, 100.0), 2)  # Arredonda o valor para duas casas decimais
            transaction = Transaction.objects.create(
                sender=sender.user,
                recipient=recipient.user,
                amount=amount,
                timestamp=timezone.now()
            )
            self.stdout.write(f'Transação de {sender.user.username} para {recipient.user.username} no valor de {amount:.2f} criada.')

        self.stdout.write('Banco de dados populado com sucesso.')