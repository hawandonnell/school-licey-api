from django.urls import path
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
	path('posts', views.PostView.as_view()),
	path('token', TokenObtainPairView.as_view()),
	path('refresh', TokenRefreshView.as_view()),
	path('posts/<int:pk>', views.PostPKView.as_view())
]
