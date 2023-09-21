from api.view.collectionView import collectionList,collectionListDetails
from django.urls import path,include



urlpatterns = [
    path('collection-list',collectionList.as_view(),name='category'),
    path('<int:pk>',collectionListDetails.as_view(),name='category-detail')
]
