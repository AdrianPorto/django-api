from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from django.utils.dateparse import parse_datetime

@api_view(['GET'])
def get_wallet_balance(request):
    try:
        wallet = Wallet.objects.get(user=request.user)
    except Wallet.DoesNotExist:
        return Response({"message": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = WalletSerializer(wallet)
    return Response(serializer.data)

@api_view(['POST'])
def add_balance(request):
    try:
        wallet = Wallet.objects.get(user=request.user)
    except Wallet.DoesNotExist:
        return Response({"message": "Wallet not found"}, status=status.HTTP_404_NOT_FOUND)
    
    amount = request.data.get('amount')
    if not amount or float(amount) <= 0:
        return Response({"message": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

    wallet.balance += float(amount)
    wallet.save()
    return Response({"message": "Balance added successfully", "balance": wallet.balance})

@api_view(['POST'])
def transfer_balance(request):
    try:
        sender_wallet = Wallet.objects.get(user=request.user)
    except Wallet.DoesNotExist:
        return Response({"message": "Sender wallet not found"}, status=status.HTTP_404_NOT_FOUND)
    
    recipient_id = request.data.get('recipient_id')
    amount = request.data.get('amount')

    if not recipient_id or not amount or float(amount) <= 0:
        return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        recipient_wallet = Wallet.objects.get(user_id=recipient_id)
    except Wallet.DoesNotExist:
        return Response({"message": "Recipient not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if sender_wallet.balance < float(amount):
        return Response({"message": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

    with transaction.atomic():
        sender_wallet.balance -= float(amount)
        sender_wallet.save()

        recipient_wallet.balance += float(amount)
        recipient_wallet.save()

        transaction_record = Transaction.objects.create(
            sender=sender_wallet.user, 
            recipient=recipient_wallet.user,  
            amount=float(amount),
            timestamp=parse_datetime(request.data.get('timestamp', ''))
        )
        transaction_record.save()

    return Response({"message": "Transfer successful", "sender_balance": sender_wallet.balance, "recipient_balance": recipient_wallet.balance})
@api_view(['GET'])

def list_transactions(request):
    start_date = request.query_params.get('start_date')
    end_date = request.query_params.get('end_date')

    print(start_date, end_date)

    transactions = Transaction.objects.filter(sender=request.user)

    if start_date:
        transactions = transactions.filter(timestamp__gte=parse_datetime(start_date))
    if end_date:
        transactions = transactions.filter(timestamp__lte=parse_datetime(end_date))

    serializer = TransactionSerializer(transactions, many=True)
    return Response(serializer.data)