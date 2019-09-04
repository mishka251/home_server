from django.db import models
from django.conf import settings
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)


class BookGenre(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    file_path = models.FilePathField(path=settings.BOOKS_HOME_DIR, recursive=True)
    genres = models.ManyToManyField(BookGenre)
