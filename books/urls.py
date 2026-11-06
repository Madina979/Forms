from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('add/', views.book_add, name='book_add'),
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]