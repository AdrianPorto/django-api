from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
def user_manager(request):
    if request.method == 'GET': 
        user_name = request.GET.get('username')  # Alterado para buscar por 'username'

        if user_name:
            try:
                user = User.objects.get(username=user_name)  
                user_data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                }
                return Response(user_data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"detail": "'username' parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'POST':
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        # Validações
        if not username or not email or not password:
            return Response({"message": "Todos os campos são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"message": "Este username já está em uso"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"message": "Este email já está em uso"}, status=status.HTTP_400_BAD_REQUEST)

        # Criação de um usuário normal
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({
            "message": "Usuário criado com sucesso",
            "id": user.id
        }, status=status.HTTP_201_CREATED)
