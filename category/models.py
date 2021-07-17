from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('category:index', kwargs={"name": self.name})
