from django.views.generic import ListView, DetailView
from articles.models import Article
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
class BlogHome(ListView):
    model = Article
    context_object_name = "articles"

# if admin is logged, we display all articles. Else, we display tje online articles.
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)

class BlogArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
