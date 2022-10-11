from django.urls import path
from app_electronic_library.views import AuthorList, BooksList, BookDetail, AuthorDetail

urlpatterns = [
    path('library/authors', AuthorList.as_view(), name='authors_list'),
    path('library/authors/<int:pk>/', AuthorDetail.as_view(), name='authors_detail'),
    path('library/books', BooksList.as_view(), name='books_list'),
    path('library/books/<int:pk>/', BookDetail.as_view(), name='books_detail'),
]