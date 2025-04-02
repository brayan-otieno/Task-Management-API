from django.urls import path
from .views import UserCreateView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
]