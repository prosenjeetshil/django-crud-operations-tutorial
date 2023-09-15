from django.urls import path
from . import views

urlpatterns = [
    path('ofv', views.orderFormView, name='order_url'),
    path('sv', views.showView, name='show_url'),
]