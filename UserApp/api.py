from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth import authenticate, login,logout
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def create_user(request):
    data = request.data 

    username = data['username']
    password = data['password']

    User.objects.create_user(username = username, password = password)

    return Response({'message': 'User created successfully!'})

# @api_view(['POST'])
# def login_user(request):
#     data = request.data

#     username = data['username']
#     password = data['password']

#     user = authenticate(username=username, password = password)

#     if user is not None:
#         login(request, user)

#         token, created = Token.objects.get_or_create(user = user)
#         return Response(
#             {'message':'User successfully logged in',
#              'token' : token.key}
#         )
#     else:
#         return Response({'message':'Invalid Credentials!'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
        return Response({
            'message' : 'Successfully authenticated',
            'username': request.user.username
        })
    