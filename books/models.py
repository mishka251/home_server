from django.db import models
from django.conf import settings


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)


class BookGenre(models.Model):
    name = models.CharField(max_length=200)


class BookInfo(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    genres = models.ManyToManyField(BookGenre)
    publish_year = models.IntegerField()


class FileTypes(models.Model):
    name = models.CharField(max_length=30)


class BookFile(models.Model):
    file_path = models.FilePathField(path=settings.BOOKS_HOME_DIR, recursive=True)
    file_type = models.ForeignKey(FileTypes, on_delete=models.CASCADE, null=True)
    size = models.DateField()
    info = models.ForeignKey(BookInfo, null=True, on_delete=models.CASCADE)
