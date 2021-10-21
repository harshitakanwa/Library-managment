from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import Magnus_Library_User
import datetime
from . import required_functions
import threading
# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['user_email']
        password = request.POST['user_password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        user_first_name = request.POST['user_first_name']
        user_last_name = request.POST['user_last_name']
        user_email = request.POST['user_email']
        user_password = request.POST['user_password']
        user_phone = request.POST['user_phone']
        user_aadhaar = request.POST['user_aadhaar']
        user_dob = request.POST['user_dob']
        user_address = request.POST['user_address']
        user_gender = request.POST['user_gender']
        user_joined_date = datetime.date.today()
        user_aadhar_photo = request.FILES['user_aadhar_photo']
        user_photo = request.FILES['user_photo']

        if Magnus_Library_User.objects.filter(user_aadhaar=user_aadhaar).exists():
            messages.info(request, 'Aadhaar already Taken')
            return redirect('register')
        if Magnus_Library_User.objects.filter(user_email=user_email).exists():
            messages.info(request, 'Email id Alredy exists')
            return redirect('register')
        if User.objects.filter(email=user_email).exists():
            messages.info(request, 'Email id Alredy exists')
            return redirect('register')
        else:
            user1 = Magnus_Library_User(
                user_first_name = user_first_name,
                user_last_name = user_last_name,
                user_phone = user_phone,
                user_email = user_email,
                user_password = user_password,
                user_aadhaar = user_aadhaar,
                user_address = user_address,
                user_dob = user_dob,
                user_gender = user_gender,
                user_joined_date = user_joined_date,
                user_aadhar_photo = user_aadhar_photo,
                user_photo = user_photo
                )
            user1.save();
            new_id = User.objects.order_by('id').last().id+1
            year = str(user_joined_date.year%100)
            username = f'{year}MLU{new_id:0004}'
            user2 = User.objects.create_user(
                username=username,
                password=user_password,
                email=user_email,
                first_name=user_first_name,
                last_name=user_last_name
                )
            user2.save()
            thread = threading.Thread(target=required_functions.send_user_details, args=(user_email, username, user_password, user_first_name))
            thread.start()
            return redirect('login')

    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def users(request):
    users = Magnus_Library_User.objects.all()
    for user in users:
        #print(user.img.url)
        pass
    return render(request,'user.html',{'users':users})