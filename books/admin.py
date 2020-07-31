from django.contrib import admin
from .models import  Author,  BookGenre
# Register your models here.



@admin.register(Author)
class AuthorBook(admin.ModelAdmin):
    pass


@admin.register(BookGenre)
class BookGenreBook(admin.ModelAdmin):
    pass
