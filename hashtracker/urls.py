
from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("api/user/login/", views.LoginAPIView.as_view(), name="user-login"),
    path("api/v1/project/",include('api.urls.project_urls')),
    # path("api/v1/category/",include('api.urls.category_urls')),
    path("api/v1/collection/",include('api.urls.collection_urls')),
   
]
