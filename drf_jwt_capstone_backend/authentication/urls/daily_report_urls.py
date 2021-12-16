from django.urls import path
from authentication import daily_report_views as views


urlpatterns = [

    path('', views.DailyReportList.as_view(), name='dailyreport'),
    path('add', views.DailyReportList.as_view(), name='dailyreport-add'),
    path('userDailyReport', views.DailyReportDetail.as_view(), name='user-dailyreport'),
    path('<int:pk>/delete', views.DailyReportDetail.as_view(), name='delete-dailyreport'),
    path('<int:pk>/update', views.DailyReportDetail.as_view(), name='delete-dailyreport'),
]