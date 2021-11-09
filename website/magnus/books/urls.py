from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name='books'),
    path('catalogue/',views.catalogue,name='catalogue'),
    path('catalogue/books/',views.books_taken,name='books_taken'),
    path('catalogue/genres/',views.genres,name='genres'),
    path('catalogue/genres/<str:genre_name>/',views.genre_books,name='genre_books'),
    path('catalogue/genres/<str:genre_name>/<int:id>/',views.book_view,name='book_view'),
    path('catalogue/genres/<str:genre_name>/<int:id>/take',views.take_book,name='take_book'),
    path('catalogue/genres/<str:genre_name>/<int:id>/return',views.return_book,name='return_book'),
    path('catalogue/genres/<str:genre_name>/<int:id>/sell',views.sell_book,name='sell_book'),
    path('catalogue/genres/<str:genre_name>/<int:id>/buy',views.buy_book,name='buy_book'),
    path('catalogue/genres/<str:genre_name>/<int:id>/request',views.request_book,name='request_book'),
]