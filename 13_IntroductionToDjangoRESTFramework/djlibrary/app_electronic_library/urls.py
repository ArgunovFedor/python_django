from django.urls import path
from app_electronic_library.views import AuthorList, BooksList

urlpatterns = [
    path('library/authors', AuthorList.as_view(), name='authors_list'),
    path('library/books', BooksList.as_view(), name='books_list')
]