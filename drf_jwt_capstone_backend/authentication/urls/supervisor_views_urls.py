from django.urls import path
from authentication import supervisor_views as views

urlpatterns = [    
    path('register', views.SupervisorView.as_view(), name='register'),
    path('profile', views.SupervisorView.as_view(), name="Supervisor-profile"),
    path('profile/update', views.SupervisorView.as_view(), name="Supervisor-profile-update"),
    path('', views.SupervisorView.as_view(), name="Supervisors"),
    path('<str:pk>', views.SupervisorView.as_view(), name='Supervisors'),
    path('update/<str:pk>', views.SupervisorView.as_view(), name='Supervisor-update'),
    path('delete/<str:pk>', views.SupervisorView.as_view(), name='Supervisor-delete'),
]
   