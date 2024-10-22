from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as Login
from django.contrib.auth import logout as auth_logout 
from .forms import UserRegisterForm
from django.urls import reverse

#register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            Login(request, user)
            return redirect('') #Redirect another page or dash
    else:
        form = UserRegisterForm()
    return render(request, 'usercred/register.html',{'form': form})

#login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            Login(request, user)
            return redirect(reverse('workstamp:home')) #Redirect another page or dash
        else:
            return render(request, 'usercred/login.html',{'error':'Please Use Correct Credentials'})  
    
    return render(request, 'usercred/login.html')        
        
#logout        
def logout(request):
    auth_logout(request)
    return redirect('login') #Back to login page       