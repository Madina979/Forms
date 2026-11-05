from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name='order'),
    path('order/result/', views.order_result, name='order_result'),
]