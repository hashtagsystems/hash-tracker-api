from django.urls import path,include
from views import categoryView



urlpatterns = [
    path('/category-list',categoryView.CategoryList.as_view(),name='category')
]
