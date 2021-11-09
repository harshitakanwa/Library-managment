from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Magnus_Library_User
from books.models import Book, BookHistory, Genres, Request
import datetime

# Create your views here.
def books(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
        except:
            return redirect('/admin')
        return redirect('catalogue')
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def genres(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            genres = Genres.objects.all()
            username = str(request.user)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
        except:
            return redirect('/admin')
        return render(request, "genres.html", {'user':user,'genres':genres,'no_of_requests':no_of_requests})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def genre_books(request,**kwargs):
    genre_name = kwargs['genre_name']
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            genre = Genres.objects.filter(genre_name=genre_name)[0]
            genre_books = Book.objects.filter(book_genre=genre)
            username = str(request.user)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
            genres = Genres.objects.all()
        except:
            return redirect('/admin')
        return render(request, "genre_books.html", {'user':user,'genres':genres,'genre_books':genre_books,'genre_name':genre_name,'no_of_requests':no_of_requests})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')


def books_taken(request,**kwargs):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            username = str(request.user)
            taken_books = Book.objects.filter(book_currentholder=username)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
            genres = Genres.objects.all()
        except:
            return redirect('/admin')
        return render(request, "books_taken.html", {'user':user,'genres':genres,'taken_books':taken_books,'no_of_requests':no_of_requests})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def catalogue(request):
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=request.user).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            books = Book.objects.all()
        except:
            return redirect('/admin')
        return redirect('genres') #render(request, "catalogue.html", {'user':user,'books':books})
    else:
        messages.info(request, 'Please login to access the book catalogue !')
        return redirect('login')

def book_view(request, *args, **kwargs):
    #print(args,kwargs)
    book_id = int(kwargs['id'])
    username = str(request.user)
    if request.user.is_authenticated:
        user_email = User.objects.filter(username=username).values()[0].get('email')
        try:
            user = Magnus_Library_User.objects.filter(user_email=user_email)[0]
            book = Book.objects.filter(id=book_id)[0]
            username = str(request.user)
            book_requests = Request.objects.filter(requested_user=username)
            no_of_requests = len(book_requests)
            genres = Genres.objects.all()
            try:
                request_status = Request.objects.filter(requesting_user=username,requested_book=book_id).values()[0]
                request_status = True
            except:
                request_status = False
            if book.book_currentholder=='Admin':
                take=True
                have_book = False
            else:
                if book.book_currentholder==username:
                    have_book = True
                else:
                    have_book = False
                take=False
            if book.book_owner==username:
                owned = True
            else:
                owned = False
            if book.book_sale==True:
                for_sale = True
            else:
                for_sale = False
            rating = book.book_rating*[0]
            context = {
                'user' : user,
                'book' : book,
                'rating' : rating,
                'take' : take,
                'owned' : owned,
                'for_sale' : for_sale,
                'request_status' : request_status,
                'have_book' : have_book,
                'no_of_requests':no_of_requests,
                'genres':genres
                }
            print(context)
        except:
            return redirect('/admin')
        return render(request, "book.html", context)
    else:
        messages.info(request, 'Please login to access the book catalogue !')
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

def return_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                try:
                    book = Book.objects.filter(id=book_id).values()[0]
                    username=str(request.user)
                    book_history = BookHistory.objects.all()
                    print(book_history)
                    book_history = BookHistory.objects.filter(book_id=book_id,book_returndate=datetime.datetime(1111,11,11).date(),book_currentholder=username)
                    print(book_history)
                    book_history.update(book_returndate=datetime.date.today())
                    for history in book_history:
                        history.save()
                    Book.objects.filter(id=book_id).update(book_currentholder='Admin')
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

def sell_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                try:
                    book = Book.objects.filter(id=book_id).values()[0]
                    Book.objects.filter(id=book_id).update(book_sale=True)
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

def buy_book(request,*args,**kwargs):
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                try:
                    book = Book.objects.filter(id=book_id).values()[0]
                    username=str(request.user)
                    Book.objects.filter(id=book_id).update(book_sale=False)
                    Book.objects.filter(id=book_id).update(book_owner=username)
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

def request_book(request,*args,**kwargs):
    print(kwargs['id'])
    if kwargs['id']:
        if request.method=='POST':
            book_id = int(request.POST['book_id'])
            if request.user.is_authenticated:
                try:
                    book = Book.objects.filter(id=book_id).values()[0]
                    username=str(request.user)
                    book_request  = Request(
                        requested_user = book.get('book_currentholder'),
                        requested_book = book_id,
                        requesting_user = username
                    )
                    print(book_request)
                    book_request.save()
                except:
                    return redirect('/admin')
                return redirect('.') #render(request, "book.html", {'user':user,'book':book,'rating':rating,'taken':taken,'owned':owned,'for_sale':for_sale})
            else:
                messages.info(request, 'Please login to access the book catalogue !')
                return redirect('login')
        else:
            return 0