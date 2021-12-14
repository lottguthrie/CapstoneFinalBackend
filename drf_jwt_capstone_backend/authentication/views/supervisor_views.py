from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from authentication.models import User
from authentication.serializers import UserSerializer, SupervisorSerializer
from rest_framework.response import Response
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password

from drf_jwt_capstone_backend.authentication.serializers import Supervisor


Supervisor = get_user_model

class SupervisorView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SupervisorSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def registerSupervisor(request):
    data = request.data

    try:
        supervisor = Supervisor.objects.create(
            SupervisorId = data['Supervisor_Id'],
            username = data['email'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = UserSerializer(supervisor, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'This email is already registered.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateSupervisorProfile(request):
    user = request.Supervisor
    serializer = UserSerializer(user, many=False)
    
    data = request.data
    User.first_name = data['name']
    User.username = data['email']
    User.email = data['email']
    if data['password'] != '':
        User.password = make_password(data['password'])
        
    User.save()
        
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSupervisorProfile(request):
    user = request.Supervisor
    
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getSupervisors(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getSupervisorById(request, pk):
    supervisor = User.objects.get(id=pk)
    serializer = UserSerializer(User, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
    user = User.objects.get(id=pk)

    data = request.data

    User.first_name = data['name']
    User.username = data['email']
    User.email = data['email']
    User.is_staff = data['isAdmin']

    User.save()

    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
    userForDeletion = User.objects.get(id=pk)
    userForDeletion.delete()
    return Response('Supervisor removed')