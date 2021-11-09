from django.urls import path
from . import views

urlpatterns = [
    path('',views.users,name='users'),
    path('notifications/',views.notifications,name='notifications'),
    path('notifications/accept',views.accept,name='notifications'),
]