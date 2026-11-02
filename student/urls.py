from django.urls import path
from . import views

urlpatterns = [
    path('', views.student, name='student'),
    path('result/', views.student_result, name='student_result'),
]