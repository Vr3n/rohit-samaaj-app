from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm

# Create your views here.


def login_view(request):
    form = LoginForm()

    msg = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember = form.cleaned_data.get("remember_me")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                if remember:
                    request.session.set_expiry(1209600)
                messages.success(request, "Logged in successfully!")
                return redirect("/")
            messages.error(request, "There are errors in credentials!")
        else:
            messages.error(request,"Error validating the form")

    context = {
        "form": form,
    }

    return render(request, "accounts/login.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully!")
    response = HttpResponseRedirect(reverse('login'))
    response["HX-Redirect"] = reverse("login")
    response["HX-Refresh"] = True
    return response

def register_view(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully!")
            return HttpResponseRedirect(reverse('login'))
        messages.error(request, "There is an error in the form!")

    return render(request, "accounts/register.html")
