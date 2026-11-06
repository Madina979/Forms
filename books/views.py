from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm


def books(request):
    all_books = Book.objects.all()
    read_count = Book.objects.filter(is_read=True).count()
    return render(request, 'books/index.html', {
        'books': all_books,
        'read_count': read_count,
        'total': all_books.count(),
    })


def book_add(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/form.html', {'form': form, 'title': 'Add book'})


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('books')
    return render(request, 'books/form.html', {'form': form, 'title': 'Edit book'})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('books')