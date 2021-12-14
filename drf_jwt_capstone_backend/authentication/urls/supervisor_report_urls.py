from django.urls import path
from authentication.views.supervisor_report_view import SupervisorReportView as views


urlpatterns = [

    path('', views.getSupervisorReport, name='supervisorreport'),
    path('add', views.addSupervisorReport, name='supervisorreport-add'),
    path('userSupervisorReport', views.getMySupervisorReport, name='user-supervisorreport'),
    path('<str:pk>/delete', views.deleteSupervisorReport, name='delete-supervisorreport'),
    path('<str:pk>/update', views.updateSupervisorReport, name='delete-supervisorreport'),
]