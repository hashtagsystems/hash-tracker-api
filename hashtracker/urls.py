
from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('user_app.urls')),
    path("api/v1/project/",include('api.urls.project_urls')),
    # path("api/v1/category/",include('api.urls.category_urls')),
    path("api/v1/collection/",include('api.urls.collection_urls')),
    path("api/v1/environment/",include('api.urls.environment_urls')),
   
]
