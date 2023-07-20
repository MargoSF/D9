from django.urls import path
from .views import PostsList, PostDetail, SearchPosts, PostsCreate, ArticlesCreate, PostEdit, PostDelete


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
   #path('category/<int:pk>', CategoryListView.as_view(), name='category_list'),
   #path('admin/', admin.site.urls),
   #path('create/', NewsCreate.as_view(), name='post_create'),
   #path('search/', PostSearch.as_view(), name='post_search'),
   #path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   #path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
   #path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]