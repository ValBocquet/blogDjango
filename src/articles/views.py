from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from articles.models import Article
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
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


class BlogArticleEdit(UpdateView):
    model = Article
    template_name = 'articles/article_edit.html'
    fields = ['title', 'content', 'published', ]
    success_url = '/'


class BlogArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy('articles:home')

