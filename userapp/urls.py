from django.urls import path
from .views import*

urlpatterns = [
   path('',home, name='home'),
   path('menu/',menu, name='menu'),
   path('about/',about, name='about'),
   path('bookseat/',bookseat, name='bookseat'),
   path('contact/',contact, name='contact'),
   path('addmenu/',addmenu, name='addmenu'),
   path('menu/delete/<int:id>',delete, name='delete'),
   path('menu/edit/<int:id>',edit, name='edit'),
   path('register/',register, name='register'),
   path('login/',login_page, name='login'),
   path('logout/',logout_page, name='logout'),
]
