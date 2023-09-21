from api.view.ProjectView import ProjectList
from django.urls import path,include



urlpatterns = [
    path('project-list',ProjectList.as_view(),name='category')
]
