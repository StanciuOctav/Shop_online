from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart


# Create your views here.
@login_required(login_url='loginPage')
def show_cart(request):
    # trebuie sa numaram de cate ori a fost adaugat fiecare produs
    user = request.user
    cart = Cart.objects.get(cart_user_id=user.id)
    cart.save()
    without_duplicates = list(dict.fromkeys(cart.cart_products))
    apperances = [cart.cart_products.count(e) for e in without_duplicates]
    dictionary = {}
    for index in range(len(without_duplicates)):
        dictionary[without_duplicates[index]] = apperances[index]
    return render(request, 'carts/show_cart.html',
                  {'user': user, 'cart': cart, "products": dictionary})
