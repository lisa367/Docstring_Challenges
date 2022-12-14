from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

# class Author(models.Model):
    # author = models.CharField(max_length=100)


User = get_user_model()


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = models.TextField(blank=True, verbose_name="Contenu")
    created_on = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    thumbnail = models.ImageField(blank=True, upload_to='MyBlog')

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    @property
    def author_or_default(self):
        return self.author.username if self.author else "Auteur anonyme"

    def get_absolute_url(self):
        return reverse('Posts:home')