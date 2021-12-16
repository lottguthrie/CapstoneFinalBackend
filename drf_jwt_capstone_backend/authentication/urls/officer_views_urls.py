from django.urls import path
from authentication import officer_views as views


urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register', views.MyTokenObtainPairView.as_view(), name='register'),
    path('profile', views.MyTokenObtainPairView.as_view(), name="users-profile"),
    path('profile/update', views.MyTokenObtainPairView.as_view(), name="users-profile-update"),
    path('', views.MyTokenObtainPairView.as_view(), name="users"),
    path('<int:pk>', views.MyTokenObtainPairView.as_view(), name='user'),
    path('update/<int:pk>', views.MyTokenObtainPairView.as_view(), name='user-update'),
    path('delete/<int:pk>', views.MyTokenObtainPairView.as_view(), name='user-delete'),
]
   
