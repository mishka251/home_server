from django.contrib import admin
from .models import  Author, Book, BookGenre
# Register your models here.


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorBook(admin.ModelAdmin):
    pass


@admin.register(BookGenre)
class BookGenreBook(admin.ModelAdmin):
    pass
