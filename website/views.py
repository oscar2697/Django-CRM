from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    if request.method == 'post':
        username = request.post['username']
        password = request.post['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You Have Been Logged In')
            return redirect('home')
        else: 
            messages.success(request, 'There was an error, Please Try Again...')
            return redirect('home')

    else:
        return render(request, 'home.html', {})

def logout_user(request):
    
