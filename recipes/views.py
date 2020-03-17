from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Home page

def home(request):
    return render(request, 'recipes/home.html')




# Main home page

def recipebook(request):
    return render(request, 'recipes/recipebook.html')





# Sign up

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'recipes/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('recipebook')
            except IntegrityError:
                return render(request, 'recipes/signupuser.html', {'form':UserCreationForm(), 'error':'Username already taken. Please try again.'})
        else:
            return render(request, 'recipes/signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match.'})



# Logout

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')




# login

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'recipes/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'recipes/loginuser.html', {'form':AuthenticationForm(), 'error': 'Username or password did not match.'})
        else:
            login(request, user)
            return redirect('recipebook')
