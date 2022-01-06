import decimal

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart
from products.models import CartProduct, Product

from .models import Order


# Create your views here.
@login_required(login_url='loginPage')
def show_cart(request):
    # trebuie sa numaram de cate ori a fost adaugat fiecare produs
    # if request.method == "GET":
    #     delete_product_from_cart(request)
    user = request.user
    cart = Cart.objects.get(cart_user_id=user.id)
    products_in_cart = CartProduct.objects.all().filter(cart_id=cart.id)  # lista de CartProducts
    products_ids = []
    for p in products_in_cart:
        products_ids.append(p.product_id)  # creating a list with only the product_id
    without_duplicates = list(dict.fromkeys(products_ids))  # deleting duplicates
    cart_products = {}  # dictionary where Key is the product and value is the number ordered
    for i in without_duplicates:
        key = Product.objects.get(id=i)
        value = CartProduct.objects.filter(product_id=key.id, cart_id=cart.id).count()
        cart_products[key] = value
    return render(request, 'carts/show_cart.html', {"products": cart_products, "cart": cart})


def delete_product_from_cart(request):
    product_name = request.GET.get('button2')
    product = Product.objects.get(product_name=product_name)
    user = request.user
    cart = Cart.objects.get(cart_user_id=user.id)
    cart_product = CartProduct.objects.filter(product_id=product.id, cart_id=cart.id)
    for cp in cart_product:
        cp.delete()


def addOrder(request):
    user = request.user
    cart = Cart.objects.get(cart_user_id=user.id)
    products_in_cart = CartProduct.objects.all().filter(cart_id=cart.id)  # lista de CartProducts
    products_ids = []
    for p in products_in_cart:
        products_ids.append(p.product_id)  # creating a list with only the product_id
    without_duplicates = list(dict.fromkeys(products_ids))  # deleting duplicates
    cart_products = {}  # dictionary where Key is the product and value is the number ordered
    for i in without_duplicates:
        key = Product.objects.get(id=i)
        value = CartProduct.objects.filter(product_id=key.id, cart_id=cart.id).count()
        cart_products[key] = value

    try:
        orders = Order.objects.get(order_user_id=user.id)
    except:
        nrOrders = Order.objects.filter(order_user_id=user.id).count()
        order = Order(order_user_id=user.id, order_order_id=nrOrders + 1)
        print(f"{user.id}")
        cart_products = CartProduct.objects.all().filter(cart_id=user.id)
        total_price = 0.0
        for cp in cart_products:
            product = Product.objects.get(id=cp.product_id)
            total_price += float(str(product.product_price))
        order.order_total_price = total_price
        order.save()

        return render(request, 'carts/orders.html', {})
