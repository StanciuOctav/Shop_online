from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserSignUpForm
from carts.models import Cart


def accountPage(request):
    if request.user.is_authenticated:
        return render(request, 'products/accountDetails.html', {'user': request.user})
    else:
        redirect('loginPage')



def create_cart(request):
    user = request.user
    try:
        Cart.objects.get(cart_user_id=user.id)
    except:
        cart = Cart(cart_user_id=user.id)
        cart.save()


def loginPage(request):
    if request.method == "POST":
        email = request.POST["email"]  # getting the email from the login page
        password = request.POST["password"]  # getting the password from the login page
        if password != "" and email != "":  # both fields were completed
            username = None
            try:
                user = User.objects.get(email=email)
                username = user.username
            except:
                messages.error(request, "User does not exist. Please try again")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                create_cart(request)
                return redirect('list_products')
            else:
                return redirect('loginPage')
        else:
            print("One of the two fields were not completed")
    else:
        return render(request, "register/login.html", {})


def logoutPage(request):
    logout(request)
    return redirect('loginPage')


def registerPage(request):
    form = UserSignUpForm()
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
        else:
            form = UserSignUpForm()
            print("Form is invalid")
    return render(request, "register/register.html", {"form": form})
