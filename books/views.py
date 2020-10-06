from typing import List

from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework import permissions
from books.serializers import UserSerializer, GroupSerializer, BookEditSerializer, BookUploadSerializer, \
    GenreSerializer, AuthorSerializer
from books.models import BookFile, BookGenre, Author
import zipfile
from django.conf import settings
import os.path
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = []  # [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = []  # [permissions.IsAuthenticated]


class BooksList(viewsets.ModelViewSet):
    queryset = BookFile.objects.all()
    # serializer_class = BookSerializer
    permission_classes = []

    def get_serializer_class(self):
        print(self.action)
        if self.action == 'list' or self.action == 'create':
            return BookUploadSerializer
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            return BookEditSerializer


class GenresView(viewsets.ModelViewSet):
    queryset = BookGenre.objects.all()
    serializer_class = GenreSerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def download(request):
    ids = request.GET.get('books', [])
    if ids:
        books = BookFile.objects.filter(id__in=ids)
    else:
        books = BookFile.objects.all()
    files = books.values('file')
    zip_response = zipfile.ZipFile('books.zip', 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        path = os.path.join(settings.MEDIA_ROOT, file['file'])
        if os.path.exists(path):
            zip_response.write(path)
    zip_response.close()
    return HttpResponse(zip_response)


# class Functions(viewsets.GenericViewSet):
#     pass

# class BookFiles(viewsets.ModelViewSet):
#     queryset = BookFile.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = []


def is_ebook(file:InMemoryUploadedFile)->bool:
    support_types = ['fb2']
    return file.name.rsplit('.', 1)[1] in support_types


def is_archive(file:InMemoryUploadedFile)->bool:
    support_types = ['zip', '7z']
    return file.name.rsplit('.', 1)[1] in support_types


def save_file(file:InMemoryUploadedFile)->List[str]:
    root = settings.MEDIA_ROOT
    if is_ebook(file):
        path = default_storage.save(file.name, ContentFile(file.read()))
        filepath = os.path.join(root, path)
        return [filepath]
    elif is_archive(file):
        zip = zipfile.ZipFile(file, 'r')
        filepaths = []
        for file_name in zip.infolist():
            content = zip.read(file_name)
            path = default_storage.save(file_name.filename, ContentFile(content))
            filepath = os.path.join(root, path)
            filepaths.append(filepath)
        return filepaths

@csrf_exempt
def load_book(request: HttpRequest):
    serializer = BookUploadSerializer(None, None)
    file:InMemoryUploadedFile = request.FILES['file']
    # if is_ebook(file):
    #     book = serializer.create(file)
    #     print(book)
    # elif is_archive(file):
    #     zip = zipfile.ZipFile(file, 'r')
    #     for file_name in zip.infolist():
    #         content = zip.read(file_name)
    #         file = InMemoryUploadedFile(content, None, file_name.filename, None, len(content), 'utf-8')
    #         book = serializer.create(file)
    #         print(book)
    filepaths = save_file(file)
    for filepath in filepaths:
        book = serializer.create(filepath)
        print(book)
    return HttpResponse(200)
    pass


def index(request: HttpRequest):
    return render(request, 'vue-main.html')
