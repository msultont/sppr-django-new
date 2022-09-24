from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout


def login(request):

    form = LoginForm()

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            # return redirect('dashboard')

        print(request.POST)

    return render(request, "index_login.html", {'login_form': form})


def logout(request):
    logout(request)
    print("sulton")
