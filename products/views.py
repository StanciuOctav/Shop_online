from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, CartProduct
from .forms import ProductForm
from carts.models import Cart


def get_cart(request):
    user = request.user
    return Cart.objects.get(cart_user_id=user.id)


def list_products(request):
    # daca se face search sau doar se afiseaza produsele
    if request.method == "POST":
        searched = request.POST["searched"].lower()  # asta se face atunci cand se apasa pe butonul de search
        products = []
        for p in Product.objects.all():
            if p.product_name.lower().find(
                    searched) > -1:  # .find() returneaza indexul la care se gaseste string ul searched si -1 daca nu l gaseste
                products.append(p)
        return render(request, "products/productsList.html", {"products": products})
    # daca se face click pe unul din butoane
    if request.method == "GET":
        cart = get_cart(request)
        if cart is None:
            cart = Cart(cart_user_id=request.user.id)
            cart.save()
        try:
            product_name_button = request.GET.get('button')
            product = Product.objects.get(product_name=product_name_button)
            cartProduct = CartProduct(product_id=product.id, cart_id=cart.id)
            cartProduct.save()
        except:
            products = Product.objects.all()
            return render(request, "products/productsList.html", {"products": products})
    products = Product.objects.all()
    return render(request, "products/productsList.html", {"products": products})


def detailed_product(request, p_name):
    product = Product.objects.get(product_name=p_name)
    return render(request, "products/productsDetails.html", {"product": product})


@login_required(login_url='loginPage')
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


@login_required(login_url='loginPage')
def delete_product(request, p_name):
    product = Product.objects.get(product_name=p_name)
    if request.method == "POST":
        yes = request.POST.get("yes")  # corespunzatoare numelui butonului
        if yes is not None:
            product.delete()
            return redirect('list_products')
    return render(request, 'products/productsDelete.html', {'product': product})


@login_required(login_url='loginPage')
def update_product(request, p_name):
    product = Product.objects.get(product_name=p_name)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_products')

    return render(request, 'products/productsUpdate.html', {'form': form})


def rename(request, username):
    return render(request, 'products/renameClient.html', {'username': username})


def renameClient(request):

    aux = request.GET.get('cautat')
    currentUser = request.user
    currentUser.username = aux
    currentUser.save()
    products = Product.objects.all()
    return render(request, "products/productsList.html", {"products": products})
