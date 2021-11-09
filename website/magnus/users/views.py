from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Magnus_Library_User
from books.models import Request,Book,BookHistory,Genres
from users.models import Tasks
import datetime

# Create your views here.
def users(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            tasks = Tasks.objects.filter(username=request.user)
            username = str(request.user)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
            no_of_books_taken = len(Book.objects.filter(book_currentholder=username))
            no_of_books_owned = len(Book.objects.filter(book_owner=username))
            genres = Genres.objects.all()
        except:
            return redirect('/admin')
        return render(request, "users.html", {'user':user,'genres':genres,'tasks':tasks,'no_of_requests':no_of_requests,'no_of_books_taken':no_of_books_taken,'no_of_books_owned':no_of_books_owned})
    else:
        messages.info(request,'Please login to access your Dashboard !')
        return redirect('login')

def take_book(request,*args,**kwargs):
    print(kwargs['id'])
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                try:
                    book = Book.objects.filter(id=book_id).values()[0]
                    history = BookHistory(
                        book_currentholder = request.user,
                        book_id = book_id,
                        book_issueddate=datetime.date.today(),
                        book_returndate=datetime.datetime(1111,11,11).date(),
                    )
                    history.save()
                    username = str(request.user)
                    Book.objects.filter(id=book_id).update(book_currentholder=username)
                    for book in Book.objects.filter(id=book_id):
                        book.save()
                except:
                    return redirect('/admin')
                return redirect('.') #render(request, "book.html", {'user':user,'book':book,'rating':rating,'taken':taken,'owned':owned,'for_sale':for_sale})
            else:
                messages.info(request, 'Please login to access the book catalogue !')
                return redirect('login')
        else:
            return 0

def accept(request):
    if request.method=='POST':
        book_id = int(request.POST['book_id'])
        requesting_user_id = request.POST['requesting_user_id']
        print(book_id)
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            tasks = Tasks.objects.filter(username=request.user)
            username = str(request.user)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
            no_of_books_taken = len(Book.objects.filter(book_currentholder=username))
            book = Book.objects.filter(id=book_id).values()[0]
            print(book)
            '''history = BookHistory(
                book_currentholder = request.user,
                book_id = book_id,
                book_issueddate=datetime.date.today(),
                book_returndate=datetime.datetime(1111,11,11).date(),
            )
            history.save()'''
            history = BookHistory.objects.filter(book_id=book_id)
            print(history[len(history)-1])
            BookHistory.objects.filter(id=history[len(history)-1].id).update(book_returndate=datetime.date.today())
            username = str(request.user)
            Book.objects.filter(id=book_id).update(book_currentholder=requesting_user_id)
            for book in Book.objects.filter(id=book_id):
                book.save()
        except:
            return redirect('/admin')
        return redirect('.')
    else:
        messages.info(request,'Please login to access your Dashboard !')
        return redirect('login')

def notifications(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            tasks = Tasks.objects.filter(username=request.user)
            username = str(request.user)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
            genres = Genres.objects.all()
        except:
            return redirect('../admin')
        return render(request, "notifications.html", {'user':user,'genres':genres,'tasks':tasks,'book_requests':book_requests,'no_of_requests':no_of_requests})
    else:
        messages.info(request,'Please login to access your Dashboard !')
        return redirect('login')

def accomplish(request):
    pass