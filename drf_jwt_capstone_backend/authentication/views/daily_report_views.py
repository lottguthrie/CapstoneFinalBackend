from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from authentication.serializers import DailyReportSerializer
from authentication.models import DailyReport


User = get_user_model()
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
        DailyReport = self.get_object(pk)
        serializer = DailyReportSerializer(DailyReport)
        return Response(serializer.data)

    def put(self,request, pk):
        DailyReport = self.get_object(pk)
        serializer = DailyReportSerializer(DailyReport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        DailyReport= self.get_object(pk)
        DailyReport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)