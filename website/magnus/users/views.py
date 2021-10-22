from django.shortcuts import redirect, render
from django.contrib.auth.models import auth, User

# Create your views here.
def users(request):
    return render(request,'users.html')