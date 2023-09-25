from api.view.environmentView import EnvironmentListCreate,EnvironmentListDeleteUpdate
from django.urls import path,include



urlpatterns = [
    path('environment-list',EnvironmentListCreate.as_view(),name='environment-list'),
    path('environment-detail/<int:pk>',EnvironmentListDeleteUpdate.as_view(),name='environment-Detail'),
]
