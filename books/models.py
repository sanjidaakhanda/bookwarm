# models.py

from django.db import models
from bookuser.models import UserAccount
from category.models import Category

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    book_detail = models.TextField()
    book_price = models.IntegerField()
    image = models.ImageField(upload_to='books/media/uploads/', blank=True, null=True)
    book_category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

class BookBorrowing(models.Model):
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE)
    book_user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.book.book_name

class BookReview(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.user_name
