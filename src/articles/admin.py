from django.contrib import admin

# Register your models here.
from articles.models import Article


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "updated_on")
    list_editable = ("published",)

admin.site.register(Article, BlogPostAdmin)