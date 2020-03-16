from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.







# Sign up

def signupuser(request):

    return render(request, 'recipes/signupuser.html', {'form':UserCreationForm()})
