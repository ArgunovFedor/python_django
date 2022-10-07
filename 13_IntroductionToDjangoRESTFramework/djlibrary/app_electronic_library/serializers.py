from rest_framework import serializers

from app_electronic_library.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'year_of_birth']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'isbn', 'year_of_release', 'number_of_pages', 'author']