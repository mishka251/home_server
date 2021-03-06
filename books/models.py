from django.db import models
from django.conf import settings


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    surname = models.CharField(max_length=200, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.name} {self.surname}'


class BookGenre(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название (параметр для авто заполнения жанра из файла)')
    verbose_name = models.CharField(max_length=200, null=True, verbose_name='Название (человеко-читаемое)')

    def __str__(self):
        return self.verbose_name or self.name


class FileTypes(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class BookFile(models.Model):
    # file_path = models.FilePathField(path=settings.BOOKS_HOME_DIR, recursive=True)
    file_type = models.ForeignKey(FileTypes, on_delete=models.CASCADE, null=True)
    file = models.FileField(null=True)
    # size = models.DateField()
    name = models.CharField(max_length=100, null=True, verbose_name='Название')
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, verbose_name='Автор')
    genres = models.ManyToManyField(BookGenre, verbose_name='Жанры')
    publish_year = models.IntegerField(null=True)
    size = models.DecimalField(null=True, decimal_places=2, max_digits=10)
