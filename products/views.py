import pymongo
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from .forms import ProductForm


def index(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "products/productsFrom.html", {"form": form})
