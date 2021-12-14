from django.urls import path
from authentication.views.supervisor_views import SupervisorView as views
from authentication.views.supervisor_views import MyTokenObtainPairView

urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register', views.registerSupervisor, name='register'),
    path('profile', views.getSupervisorProfile, name="Supervisor-profile"),
    path('profile/update', views.updateSupervisorProfile, name="Supervisor-profile-update"),
    path('', views.getSupervisor, name="Supervisors"),
    path('<str:pk>', views.getSupervisorById, name='Supervisors'),
    path('update/<str:pk>', views.updateSupervisor, name='Supervisor-update'),
    path('delete/<str:pk>', views.deleteSupervisor, name='Supervisor-delete'),
]
   