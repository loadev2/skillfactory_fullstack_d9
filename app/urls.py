from app.views import PostList, PostDetail, PostCreate, CategoriesList, CategoryDetails
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('post/create/', PostCreate.as_view(), name='post-create'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategoriesList.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetails.as_view(), name='category-detail'),
]