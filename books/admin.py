from django.contrib import admin
from books.models import Book,BookBorrowing,BookReview

# Register your models here.
admin.site.register(Book)
admin.site.register(BookBorrowing)
admin.site.register(BookReview)