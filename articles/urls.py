from django.urls import path
from .views import ArticleListView
from.views import ArticleDetailView,ArticleUpdateView,ArticleDeleteView,ArticleCreateView
urlpatterns = [
           path('', ArticleListView.as_view(), name='article_list'),

           path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), # new
           path('<int:pk>/',ArticleDetailView.as_view(), name='article_detail'), # new
           path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete') ,# new
           path('new/', ArticleCreateView.as_view(), name='article_new'), # new
]