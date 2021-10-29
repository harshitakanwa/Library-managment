from django.db import models

# Create your models here.
class Book(models.Model):
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
        ('children','Children')
        ]
    book_name=models.CharField(max_length=30)
    book_isbn=models.PositiveIntegerField()
    book_author=models.CharField(max_length=40)
    book_publicaton=models.CharField(max_length=50)
    book_category=models.CharField(max_length=30,choices=book_catchoice,default='education')
    book_typechoice=[
        ('HardCopy', 'HardCopy'),
        ('softCopy', 'Softcopy')
        ]
    book_type=models.CharField(max_length=30,choices=book_typechoice,default='HardCopy')
    book_quantity=models.PositiveIntegerField()
    book_pages=models.PositiveIntegerField()
    book_age_rating=models.RatingField(range=100)
    book_rating=models.RatingField(range=5)
    book_price=models.PositiveIntegerField()
    book_edition=models.PositiveIntegerField()
    book_dateofpurchase=models.DateTimeField()
    book_currentholder=models.CharField(max_length=30, default='Admin')


class BookHistory(models.Model):
    book_currentholder=models.CharField(max_length=30)
    book_id=models.CharField(max_length=30)
    book_issueddate=models.DateTimeField()
    book_returndate=models.DateTimeField()
    book_fine=models.PositiveIntegerField(default=0)
    

