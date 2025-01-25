from django.contrib.auth import authenticate, login,logout
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"message": "Email e senha são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)


    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        login(request, user)  # Faz o login do usuário
        tokens = get_tokens_for_user(user)  # Gera o token JWT
        return Response({
            "message": "Login bem-sucedido",
            "username": user.username,
            "tokens": tokens  # Envia os tokens JWT
        }, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Credenciais inválidas"}, status=status.HTTP_400_BAD_REQUEST)


# Logout do usuário
@api_view(['POST'])
def logout_view(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return Response({"message": "Usuário não autenticado"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Logout bem-sucedido"}, status=status.HTTP_200_OK)
