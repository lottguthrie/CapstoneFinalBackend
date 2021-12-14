from django.urls import path
from authentication.views import supervisor_report_view as views


urlpatterns = [

    path('', views.SupervisorReportList.as_view(), name='supervisorreport'),
    path('add', views.SupervisorReportList.as_view(), name='supervisorreport-add'),
    path('userSupervisorReport/<int:pk>', views.SupervisorReportList.as_view(), name='user-supervisorreport'),
    path('<int:pk>/delete', views.SupervisorReportDetail.as_view(), name='delete-supervisorreport'),
    path('<int:pk>/update', views.SupervisorReportDetail.as_view(), name='update-supervisorreport'),
]