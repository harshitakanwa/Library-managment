from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Magnus_Library_User

# Create your views here.
def books(request):
    if request.user.is_authenticated:
        print(request.user)
        #dests = Magnus_Library_User.objects.all()
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        print(user_email)
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
        except:
            return redirect('../admin')
        print(user)
        print(user_email)
        return render(request, "books.html", {'user':user})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')
