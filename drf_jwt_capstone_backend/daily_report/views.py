from django.shortcuts import render
from .models import DailyReport
from .serializers import DailyReportSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.serializers import Serializer

from .serializers import DailyReportSerializer




# Create your views here.
class DailyReportView(generics.CreateAPIView):
    queryset = DailyReport.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = DailyReportSerializer

class DailyReportList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        dailyreport = DailyReport.objects.all()
        serializer = DailyReportSerializer(dailyreport, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DailyReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DailyReportDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return DailyReport.objects.get(pk=pk)
        except DailyReport.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        dailyreport = self.get_object(pk)
        serializer = DailyReportSerializer(dailyreport)
        return Response(serializer.data)

    def put(self,request, pk):
        dailyreport = self.get_object(pk)
        serializer = DailyReportSerializer(dailyreport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dailyreport= self.get_object(pk)
        dailyreport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)