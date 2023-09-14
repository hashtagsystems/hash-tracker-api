
from django.urls import path,include
from .views import CategoryList



urlpatterns = [

        path('category/',CategoryList.as_view(),name='category')
]
