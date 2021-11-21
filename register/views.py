from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm


# Create your views here.
def login(request):
    if request.method == "POST":
        email = request.POST["email"]  # getting the email from the login page
        password = request.POST["password"]  # getting the password from the login page
        if password != "" and email != "":  # both fields were completed
            try:
                user = Client.objects.get(email=email)  # getting the user with the email introduced
                if user.password == password:  # if the user's password corresponds to the one introduced
                    return redirect("products/show/")
                else:
                    print("Wrong password")
            except:
                print("It doesn't exist an user with this password")
        else:
            print("One of the two fields were not completed")
    return render(request, "register/login.html", {})


def register(request):
    form = ClientForm()
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = ClientForm()
            print("Form is invalid")
    return render(request, "register/register.html", {"form": form})
