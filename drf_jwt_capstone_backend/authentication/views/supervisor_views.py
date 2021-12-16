from rest_framework import generics
from authentication.models import User
from authentication.serializers import SupervisorSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from authentication.serializers import Supervisor


class SupervisorView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SupervisorSerializer

@api_view(['POST'])
def registerSupervisor(request):
    data = request.data

    try:
        supervisor = Supervisor.objects.create(

            SupervisorId = data['Supervisor_Id'],
            last_name = data['last_name'],
            badge_number = data['badge_number'],
            password = make_password(data['password'])
        )
        serializer = SupervisorSerializer(supervisor, many=False)
        return Response(serializer.data)
    except:
        message = {'detail':'This Supervisor is already registered.'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateSupervisorProfile(request):
    Supervisor = request.Supervisor
    serializer = SupervisorSerializer(Supervisor, many=False)
    
    data = request.data
    Supervisor.first_name = data['firsrtname']
    Supervisor.last_name = data['lastname']
    Supervisor.badge_number= data['badgenumber']
    if data['password'] != '':
        User.password = make_password(data['password'])
        
    User.save()
        
    return Response(serializer.data)


@api_view(['GET'])
def getSupervisorProfile(request):
    Supervisor = request.Supervisor
    
    serializer = SupervisorSerializer(Supervisor, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getSupervisors(request):
    Supervisor = User.objects.all()
    serializer = SupervisorSerializer(Supervisor, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSupervisorById(request, pk):
    Supervisor = User.objects.get(id=pk)
    serializer = SupervisorSerializer(Supervisor, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateUser(request, pk):
    Supervisor = User.objects.get(id=pk)

    data = request.data

    Supervisor.first_name = data['firsrtname']
    Supervisor.last_name = data['lastname']
    Supervisor.badge_number= data['badgenumber']
    

    Supervisor.save()

    serializer = SupervisorSerializer(Supervisor, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteSupervisor(request, pk):
    SupervisorForDeletion = User.objects.get(id=pk)
    SupervisorForDeletion.delete()
    return Response('Supervisor removed')