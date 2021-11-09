from django.contrib import admin
from .models import BookHistory,Book,Fine, Request,Subscription, Genres

# Register your models here.
admin.site.register(Book)
admin.site.register(BookHistory)
admin.site.register(Fine)
admin.site.register(Subscription)
admin.site.register(Request)
admin.site.register(Genres)

