from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import AddProductForm


def home(request):
    return render(request, 'app/home.html')


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added!')
            return HttpResponseRedirect(reverse('app:home'))
    else:
        form = AddProductForm()
    return render(request, 'app/add-product.html', {'form': form})
