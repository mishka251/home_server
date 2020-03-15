from django.shortcuts import render

# Create your views here.
from django.views import View
from books.models import BookInfo, BookGenre, Author
from django.template.response import TemplateResponse

class BookListView(View):

    def get(self, request):
        objects = BookInfo.objects.all()

        template = "book_list.html"

        return TemplateResponse(request, template, {'books':objects})


class BookObjectView(View):

    def get(self, request, pk):
        object = BookInfo.objects.get(pk=pk)

        template = "book.html"

        return TemplateResponse(request, template, {'books': object})