from django.db import models
from django.urls import reverse

from post.models import Post
# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nome')
    content = models.TextField(verbose_name='Comentário')
    published = models.BooleanField(default=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def get_asolute_url(self):
        return reverse('comment:create', kwargs={'slug': self.post.slug})
