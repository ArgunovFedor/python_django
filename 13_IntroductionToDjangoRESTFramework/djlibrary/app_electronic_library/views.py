from rest_framework.mixins import ListModelMixin, CreateModelMixin
from django.db.models import Count
from app_electronic_library.models import Book, Author
from app_electronic_library.serializers import BookSerializer, AuthorSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5


class BooksList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Book.objects.all()
        book_author = self.request.query_params.get('author')
        book_name = self.request.query_params.get('name')
        # должно приходить в формате текста <2 или =2 или >2
        number_of_pages = self.request.query_params.get('number_of_pages')
        if book_author and book_name:
            author = Author.objects.get(name=book_author)
            queryset = queryset.filter(author_id=author.id, name=book_name)
        elif book_author:
            author = Author.objects.get(name=book_author)
            queryset = queryset.filter(author_id=author.id)
        elif book_name:
            queryset = queryset.filter(name=book_name)
        if number_of_pages:
            if number_of_pages[0] in ['>', '<', '=']:
                number = ['>', '<', '='].index(number_of_pages[0])
                if number == 0:
                    queryset = list(filter(lambda x: x.number_of_pages > int(number_of_pages[1:]), queryset))
                elif number == 1:
                    queryset = list(filter(lambda x: x.number_of_pages < int(number_of_pages[1:]), queryset))
                else:
                    queryset = list(filter(lambda x: x.number_of_pages == int(number_of_pages[1:]), queryset))
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class AuthorList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Author.objects.all()
        book_author = self.request.query_params.get('name')
        if book_author:
            queryset = queryset.filter(name=book_author)
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
