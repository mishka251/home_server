from django.contrib.auth.models import User, Group
from rest_framework import serializers
import ebookmeta
from books.models import BookFile, BookGenre, Author
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


class BookUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookFile
        #fields = ['file']
        exclude = []

    def create(self, file_path:str):
        #print(validated_data)
        #file: InMemoryUploadedFile = validated_data.get('file')
        # content: bytes = file.read()
        metadata = ebookmeta.get_metadata(file_path)
        author_name, author_surname = metadata.author[0].split(' ')
        author = Author.objects.get_or_create(name=author_name, surname=author_surname)[0]
        genres = list(map(lambda genre_name: BookGenre.objects.get_or_create(name=genre_name)[0], metadata.tag))
        res: BookFile = BookFile() #super().create(validated_data)
        res.author = author
        res.save()
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
