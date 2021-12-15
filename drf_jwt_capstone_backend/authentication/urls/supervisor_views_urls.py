from django.urls import path
from authentication.views.supervisor_views import MyTokenObtainPairView, MyTokenObtainPairSerializer
from authentication.views import supervisor_views as views

urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),     
    path('register', views.MyTokenObtainPairView.as_view(), name='register'),
    path('profile', views.MyTokenObtainPairView.as_view(), name="Supervisor-profile"),
    path('profile/update', views.MyTokenObtainPairView.as_view(), name="Supervisor-profile-update"),
    path('', views.MyTokenObtainPairView.as_view(), name="Supervisors"),
    path('<str:pk>', views.MyTokenObtainPairView.as_view(), name='Supervisors'),
    path('update/<str:pk>', views.MyTokenObtainPairView.as_view(), name='Supervisor-update'),
    path('delete/<str:pk>', views.MyTokenObtainPairView.as_view(), name='Supervisor-delete'),
]
   