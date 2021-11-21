from django.shortcuts import render, redirect


from .models import Product
from .forms import ProductForm


def list_products(request):
    if request.method == "POST":
        searched = request.POST["searched"].lower()  # asta se face atunci cand se apasa pe butonul de search
        products = []
        for p in Product.objects.all():
            if p.product_name.lower().find(
                    searched) > -1:  # .find() returneaza indexul la care se gaseste string ul searched si -1 daca nu l gaseste
                products.append(p)
        return render(request, "products/productsList.html", {"products": products})
    else:
        products = Product.objects.all()
        return render(request, "products/productsList.html", {"products": products})


def detailed_product(request, p_name):
    product = Product.objects.get(product_name=p_name)
    return render(request, "products/productsDetails.html", {"product": product})


def create_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_products")
        else:
            ProductForm()
            return redirect("create_product")
    return render(request, "products/productsForm.html", {"form": form})


def delete_product(request, p_name):
    product = Product.objects.get(product_name=p_name)
    if request.method == "POST":
        yes = request.POST.get("yes")  # corespunzatoare numelui butonului
        if yes is not None:
            product.delete()
            return redirect('list_products')
    return render(request, 'products/productsDelete.html', {'product': product})


def update_product(request, p_name):
    product = Product.objects.get(product_name=p_name)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')

    return render(request, 'products/productsUpdate.html', {'form': form})
