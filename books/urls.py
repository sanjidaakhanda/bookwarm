from django.urls import path
from books.views import BookDetailsView,BookBorrowView,BorrowBookListView,BookReturnView

urlpatterns = [
    path('details/<int:pk>/', BookDetailsView.as_view(), name='details'),
    path('details/<int:pk>/add_comment/', BookDetailsView.as_view(), name='add_comment'),
    path('borrow_book/<int:id>/', BookBorrowView.as_view(), name='borrow_book'),
    path('borrow_book_lists/', BorrowBookListView.as_view(), name='borrow_book_lists'),
    path('return_book/<int:id>/', BookReturnView.as_view(), name='return_book'),
]