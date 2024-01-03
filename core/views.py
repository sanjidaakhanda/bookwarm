
from django.shortcuts import render
from django.views.generic import ListView
from books.models import Book
from category.models import Category
from django.shortcuts import get_object_or_404


class HomeView(ListView):
    template_name = 'home.html'
    model = Book
    context_object_name = 'books'
   

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = Book.objects.filter(book_category=category)
        else:
            queryset = Book.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
