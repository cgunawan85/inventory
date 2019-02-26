from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import AddProductForm, AddVendorForm, InTransactionForm, OutTransactionForm


def home(request):
    return render(request, 'app/home.html')


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            messages.success(request, 'Product added!')
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = AddProductForm()
    return render(request, 'app/add-product.html', {'form': form})


def in_transaction(request):
    if request.method == 'POST':
        form = InTransactionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            product = form.product
            product.stock = product.stock + form.quantity
            product.save()
            messages.success(request, 'Product inventory updated')
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = InTransactionForm()
    return render(request, 'app/in-transaction-form.html', {'form': form})


def out_transaction(request):
    if request.method == 'POST':
        form = OutTransactionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            product = form.product
            product.stock = product.stock - form.quantity
            product.save()
            if product.stock < product.reorder_limit:
                send_low_stock_email(request, product=product.name, warehouse=product.warehouse)
                print('Log: reorder email sent')
            messages.success(request, 'Product inventory updated')
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = OutTransactionForm()
    return render(request, 'app/out-transaction-form.html', {'form': form})


def add_vendor(request):
    if request.method == 'POST':
        form = AddVendorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vendor added!')
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = AddVendorForm()
    return render(request, 'app/add-vendor.html', {'form': form})


def send_low_stock_email(request, product, warehouse):
    subject = product + ' in ' + warehouse + ' is running low'
    message = 'Test'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['chris@restodepot.id', ]
    send_mail(subject, message, email_from, recipient_list)
