from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login

def home(request):
    return render(request, 'index.html',{
        'message': 'nuevo mensaje desde la vista',
        'products': [
            {'id': 1, 'name': 'Producto 1', 'price': 100, 'stock': 0},
            {'id': 2, 'name': 'Producto 2', 'price': 200, 'stock': 20},
            {'id': 3, 'name': 'Producto 3', 'price': 300, 'stock': 30},
        ]
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            print("Incorrecto")
            
    return render(request, 'users/login.html')