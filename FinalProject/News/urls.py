from django.urls import path
from .views import PostsList, PostDetail, SearchPosts, PostsCreate, ArticlesCreate, PostEdit, PostDelete
from News.views import CategoryListView
from .models import Category
from .views import subscribe


urlpatterns = [
   path('', PostsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view()),
   path('posts/search/', PostDetail.as_view()),
   path('posts/create/', PostsCreate.as_view(), name='posts_create'),
   path('articles/create/', ArticlesCreate.as_view(), name='article_create'),
   path('posts/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('articles/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('posts/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]