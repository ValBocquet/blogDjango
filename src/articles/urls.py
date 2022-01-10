from django.urls import path
from articles.views import BlogHome

from articles.views import BlogArticleDetail, BlogArticleEdit, BlogArticleDelete

app_name = "articles"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('edit/<str:slug>/', BlogArticleEdit.as_view(), name="edit"),
    path('<str:slug>/', BlogArticleDetail.as_view(), name="article"),
    path('delete/<str:slug>/', BlogArticleDelete.as_view(), name="delete"),
]