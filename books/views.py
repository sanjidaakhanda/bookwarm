# views.py

from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Book, BookBorrowing, BookReview
from books.forms import ReviewForm
from django.utils import timezone
from transactions.views import send_email

class BookDetailsView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.reviews.all()
        context['form'] = ReviewForm()
        context['reviews'] = reviews
        return context

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect('details', pk=book.id)

        return self.render_to_response(self.get_context_data(form=form))

class BookBorrowView(LoginRequiredMixin, View):
    def get(self, request, id, **kwargs):
        book = get_object_or_404(Book, id=id)
        user = self.request.user
        if user.account.balance > book.book_price:
            user.account.balance -= book.book_price
            messages.success(request, 'book borrowed successful')
            user.account.save(update_fields=['balance'])
            BookBorrowing.objects.create(
                book=book,
                book_user=request.user.account,
                created_on=timezone.now(),
            )
            send_email(user, book.book_price, 'borrow', 'Book Borrow Message', 'email_temp.html')
            return redirect('borrow_book_lists')
        else:
            messages.error(request, 'Insufficient balance to borrow the book')
            return redirect('home')

class BorrowBookListView(LoginRequiredMixin, ListView):
    model = BookBorrowing
    template_name = 'borrowed_book.html'
    context_object_name = 'borrowed_books'

    def get_queryset(self):
        user_id = self.request.user.id
        queryset = BookBorrowing.objects.filter(book_user__user_id=user_id)
        return queryset

class BookReturnView(LoginRequiredMixin, View):
    def get(self, request, id,  **kwargs):
        book = get_object_or_404(BookBorrowing, id=id)
        user = self.request.user
        user.account.balance += book.book.book_price
        messages.success(request, 'book return successful')
        user.account.save(update_fields=['balance'])
        send_email(user, book.book.book_price, 'return_book', 'Book Return Message', 'email_temp.html')
        book.delete()
        return redirect('borrow_book_lists')
