from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-product/', views.add_product, name='add-product'),
    path('in-transaction-form/', views.in_transaction, name='in-transaction-form'),
    path('out-transaction-form/', views.out_transaction, name='out-transaction-form'),
]
