from django.db import models
from django.db.models.expressions import ValueRange


# Create your models here.

'''def create_book_id():
    new_id = Book_id.objects.order_by('id').last().id+1
    year = str(datetime.date.today().year%100)
    book_id = f'{year}MLB{new_id:00000008}'
    return book_id
'''
DEFAULT_GENRE_ID = 1
class Book(models.Model):
    book_name=models.CharField(max_length=100)
    book_isbn=models.PositiveIntegerField()
    book_author=models.CharField(max_length=40)
    book_publicaton=models.CharField(max_length=50)
    book_genre=models.ForeignKey('Genres',on_delete=models.CASCADE,default=DEFAULT_GENRE_ID)
    book_typechoice=[
        ('HardCopy', 'Hard Copy'),
        ('SoftCopy', 'Soft Copy')
        ]
    book_type=models.CharField(max_length=30,choices=book_typechoice,default='HardCopy')
    book_quantity=models.PositiveIntegerField()
    book_pages=models.PositiveIntegerField()
    book_age_rating=models.PositiveIntegerField(default=3)
    book_rating=models.PositiveIntegerField(default=1)
    book_price=models.PositiveIntegerField()
    book_edition=models.PositiveIntegerField()
    book_dateofpurchase=models.DateTimeField()
    book_currentholder=models.CharField(max_length=30, default='Admin')
    book_description = models.TextField(default='')
    book_image = models.ImageField(upload_to = 'book_photos',default='book_photos/photo.png')
    book_owner = models.CharField(max_length=30, default='Admin')
    book_sale = models.BooleanField(default=False)
    def __str__(self):
         return self.book_name


class BookHistory(models.Model):
    book_currentholder=models.CharField(max_length=30)
    book_id=models.CharField(max_length=30)
    book_issueddate=models.DateTimeField()
    book_returndate=models.DateTimeField()
    book_fine=models.PositiveIntegerField(default=0)

class Fine(models.Model):
    username=models.PositiveIntegerField()
    book_id=models.PositiveIntegerField()
    fine=models.PositiveIntegerField(default=0)
    paid_status=models.BooleanField(default=True)
    paid_date=models.DateField()

class Subscription(models.Model):
    subscription_choice=[
        ('Basic','Basic'),
        ('Prime','Prime')
    ]
    subscription_type=models.CharField(max_length=30,choices=subscription_choice,default=0)
    subscription_amount=models.PositiveIntegerField(default=0)
    max_no_books=models.PositiveIntegerField(default=4)

class Request(models.Model):
    requested_user = models.CharField(max_length=30)
    requested_book = models.PositiveIntegerField()
    requesting_user = models.CharField(max_length=30)
    request_status = models.BooleanField(default=False)
    
class Genres(models.Model):
    book_catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi'),
        ('children','Children'),
        ('science','Science')
        ]
    genre_name=models.CharField(max_length=30,choices=book_catchoice,default='education')
    genre_image = models.ImageField(upload_to='genre_photos',default ='genre_photos/genre_default.jpg' )
    
    def __str__(self):
         return self.genre_name
