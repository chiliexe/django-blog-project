from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from category.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    summary = models.TextField(max_length=150, verbose_name='Resumo')
    content = models.TextField(verbose_name='Conteudo')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/', verbose_name='Imagem')
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:detail', kwargs={"slug": self.slug})
