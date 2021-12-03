from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from daily_report.views import DailyReportView
from supervisor_report.views import SupervisorReportView



urlpatterns = [    

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dailyreport/', DailyReportView.as_view(), name='daily_report'),
    path('supervisorreport/', SupervisorReportView.as_view(), name='supervisor_report'),
]


