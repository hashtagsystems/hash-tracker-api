
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("api/user/login/", views.LoginAPIView.as_view(), name="user-login"),
]
