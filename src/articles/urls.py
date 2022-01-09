from django.urls import path
from articles.views import BlogHome

from articles.views import BlogArticleDetail

app_name = "articles"

urlpatterns = [
    path('', BlogHome.as_view(), name="home"),
    path('<str:slug>/', BlogArticleDetail.as_view(), name="article"),
]