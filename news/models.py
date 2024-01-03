from django.db import models
from news.verifications import title_verify


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    password = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=200, blank=False, validators=[title_verify]
    )
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(blank=False)
    image = models.ImageField(upload_to="img/", blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
