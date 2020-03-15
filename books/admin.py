from django.contrib import admin
from .models import  Author, BookInfo, BookGenre
# Register your models here.


@admin.register(BookInfo)
class AdminBook(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorBook(admin.ModelAdmin):
    pass


@admin.register(BookGenre)
class BookGenreBook(admin.ModelAdmin):
    pass
