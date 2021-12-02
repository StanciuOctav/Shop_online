from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



# Create your views here.
def loginPage(request):
    if request.method == "POST":
        email = request.POST["email"]  # getting the email from the login page
        password = request.POST["password"]  # getting the password from the login page
        if password != "" and email != "":  # both fields were completed
            # client = User.objects.get(email=email)  # getting the user with the email introduced
            userUser = User.objects.get(email=email)
            print(f"Username:{userUser.username} Password:{userUser.password}")
            userToLogin = authenticate(request, username=userUser.username, password=password)
            print(f"UserToLogin: {userToLogin}")
            # login(request, userToLogin)
            if userToLogin is not None:
                print(f"Username:{userToLogin.username} Password:{userToLogin.password}")
                return redirect('list_products')
            else:
                return redirect('loginPage')
        else:
            print("One of the two fields were not completed")
    else:
        return render(request, "register/login.html", {})


def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginPage')
        else:
            form = UserCreationForm()
            print("Form is invalid")
    return render(request, "register/register.html", {"form": form})
