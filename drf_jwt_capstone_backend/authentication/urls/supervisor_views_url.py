from django.urls import path
from authentication.views.supervisor_views import MyTokenObtainPairView
from authentication.views import supervisor_views as views

urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
         
    path('register', views.registerSupervisor.as_view(), name='register'),
    path('profile', views.getSupervisorProfile.as_view(), name="Supervisor-profile"),
    path('profile/update', views.updateSupervisorProfile.as_view(), name="Supervisor-profile-update"),
    path('', views.getSupervisors.as_view(), name="Supervisors"),
    path('<str:pk>', views.getSupervisorById.as_view(), name='Supervisors'),
    path('update/<str:pk>', views.updateUser.as_view(), name='Supervisor-update'),
    path('delete/<str:pk>', views.deleteUser.as_view(), name='Supervisor-delete'),
]
   