from typing import Optional

from django.contrib.auth.models import User, Group
from rest_framework import serializers
import ebookmeta
from books.models import BookFile, BookGenre, Author, FileTypes
from django.conf import settings
import os.path


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


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'caption']

    caption = serializers.SerializerMethodField()

    def get_caption(self, obj):
        return str(obj)


class BookUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        # fields = ['file']
        exclude = []

    author = BookAuthorSerializer()
    file_type = serializers.StringRelatedField()

    def create(self, file_path: str, author_id: Optional[int]):
        metadata = ebookmeta.get_metadata(file_path)
        author: Author = None
        if author_id is not None:
            author = Author.objects.get(id=author_id)
        else:
            author_surname, author_name, *_ = metadata.author_sort[0].split(' ')
            author = Author.objects.get_or_create(name=author_name, surname=author_surname)[0]
        genres = list(map(lambda genre_name: BookGenre.objects.get_or_create(name=genre_name)[0], metadata.tag))
        res: BookFile = BookFile()  # super().create(validated_data)
        res.author = author
        res.name = metadata.title
        res.save()
        res.genres.add(*genres)
        res.file = file_path
        file_type = FileTypes.objects.get_or_create(name=metadata.format)[0]
        res.file_type = file_type
        res.size = os.stat(file_path).st_size / 1024
        res.save()
        return res


class BookEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        # fields = ['__all__']
        exclude = []

    author = BookAuthorSerializer()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = []


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        exclude = []
