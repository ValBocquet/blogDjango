from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField()
    author = models.TextField()
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('blog_post_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return self.title