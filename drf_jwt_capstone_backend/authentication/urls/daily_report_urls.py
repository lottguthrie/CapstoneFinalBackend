from django.urls import path
from authentication.views.daily_report_views import DailyReport as views


urlpatterns = [

    path('', views.getDailyReport, name='dailyreport'),
    path('add', views.addDailyReport, name='dailyreport-add'),
    path('userDailyReport', views.getUserDailyReport, name='user-dailyreport'),
    path('<str:pk>/delete', views.deleteDailyReport, name='delete-dailyreport'),
    path('<str:pk>/update', views.updateDailyReport, name='delete-dailyreport'),
]