from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# models.py imports

from .models import Recipe

# forms.py imports

from .forms import CreateUserForm



# Sign up

def signupuser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        # try:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('first_name')

                return redirect('recipebook')
                messages.success(request, 'Account was created for ' + user )
        # except IntegrityError:
        #     return render(request, 'recipes/signupuser.html', {'form':CreateUserForm(), 'error':'Username already taken. Please try again.'})

    context = {'form':form}
    return render(request, 'recipes/signupuser.html', context)



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




# Home page

def home(request):
    # recipes = Recipe.objects.all()
    return render(request, 'recipes/home.html')




# Recipe Library page

def recipebook(request):
    recipes = Recipe.objects.order_by('-created')[:5]
    return render(request, 'recipes/recipebook.html', {'recipes':recipes})



# Solo recipe with instructions

def solo(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/solo.html', {'recipe':recipe})
