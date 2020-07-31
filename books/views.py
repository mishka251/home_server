from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets, serializers
from rest_framework import permissions
from books.serializers import UserSerializer, GroupSerializer, BookEditSerializer, BookUploadSerializer, \
    GenreSerializer, AuthorSerializer
from books.models import BookFile, BookGenre, Author
import zipfile
from django.conf import settings
import os.path


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


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
