from django.shortcuts import render
from .models import SupervisorReport
from .serializers import SupervisorReportSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import SupervisorReportSerializer



# Create your views here.
class SupervisorReportView(generics.CreateAPIView):
    queryset = SupervisorReport.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SupervisorReportSerializer

class SupervisorReportList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        supervisorreport = SupervisorReport.objects.all()
        serializer = SupervisorReportSerializer(supervisorreport, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupervisorReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SupervisorReportDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return SupervisorReport.objects.get(pk=pk)
        except SupervisorReport.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        supervisorreport = self.get_object(pk)
        serializer = SupervisorReportSerializer(supervisorreport)
        return Response(serializer.data)

    def put(self,request, pk):
        supervisorreport = self.get_object(pk)
        serializer = SupervisorReportSerializer(supervisorreport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        supervisorreport= self.get_object(pk)
        supervisorreport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)