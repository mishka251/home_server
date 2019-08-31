from django.contrib import admin
from .models import  Author, Book, BookGenre
# Register your models here.


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass


