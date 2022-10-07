from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout


def login(request, stateargs='sppr'):

    form = LoginForm()

    if request.method == 'POST':
        # TODO 1: Implementasikan request.method agar menerima value pilihan dari template 
        email = request.POST['email']
        password = request.POST['password']
        state = request.POST['state']
        # print(request.POST)
        # user = authenticate(request, username=email, password=password)

        # if user is not None:
        #     auth_login(request, user)

        # TODO 2: Implementasikan redirect() berdasarkan pilihan SPPR atau SRUPDT. Jika SPPR, redirect('dashboard-sppr'). Jika SRUPDT, redirect('dashboard-srupdt)
        if state == 'sppr':
            return redirect('index_sppr')
        elif state == 'srupdt':
            return redirect('index_srupdt')
        elif state == 'sipasti':
            return redirect('index_sipasti')
        else:
            return
        
    return render(request, "index_login.html", {'login_form': form, 'state': stateargs})


def logout(request):
    logout(request)
    print("sulton")
