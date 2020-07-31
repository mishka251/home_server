from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers
import ebookmeta
from books.models import BookFile, BookGenre, Author
from django.conf import settings
import os.path

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        exclude = []


class BookUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        fields = ['file']
        # exclude = []

    def create(self, validated_data):
        print(validated_data)
        file: InMemoryUploadedFile = validated_data.get('file')
        # content: bytes = file.read()
        root = settings.MEDIA_ROOT
        path = default_storage.save(file.name, ContentFile(file.read()))
        filepath = os.path.join(root, path)
        metadata = ebookmeta.get_metadata(filepath)
        author_name, author_surname = metadata.author[0].split(' ')
        author = Author.objects.get_or_create(name=author_name, surname=author_surname)[0]
        genres = list(map(lambda genre_name: BookGenre.objects.get_or_create(name=genre_name)[0], metadata.tag))
        res: BookFile = super().create(validated_data)
        res.author = author
        res.genres.add(*genres)
        res.save()
        return res


class BookEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        # fields = ['__all__']
        exclude = []


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        exclude = []
