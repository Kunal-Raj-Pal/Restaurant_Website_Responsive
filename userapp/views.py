from django.shortcuts import render, redirect
from .models import*
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(req):
    item = AddMenu.objects.all()
    return render(req, 'home.html',{'item':item})



def menu(req):
    item = AddMenu.objects.all()
    return render(req, 'menu.html',{'item':item})


def about(req):
    return render(req, 'about.html')


def bookseat(req):
    if req.method == "POST":
        name = req.POST.get('name')
        phone = req.POST.get('phone')
        email = req.POST.get('email')
        nop = req.POST.get('no.p')

        seatbooker = BookSeatData(name=name, phone=phone, email=email, nop=nop)
        seatbooker.save()
        print(name,phone,email,nop)
        return redirect('bookseat')


    return render(req, 'bookseat.html')

def contact(req):
    if req.method == "POST":
        name = req.POST.get('name')
        phone = req.POST.get('phone')
        email = req.POST.get('email')
        feed = req.POST.get('feed')

        seatbooker = FeedbackOrContactData(name=name, phone=phone, email=email, feed=feed)
        seatbooker.save()
        print(name,phone,email,feed)
    return render(req, 'contact.html')

@login_required
def addmenu(req):
    if req.method == "POST":
        item = req.POST.get('menuitem')
        items = AddMenu(item=item)
        items.save()
        messages.success(req,'Menu added successfully!')
        return redirect('addmenu')

    return render(req, 'addmenu.html')

def delete(req, id):
    item = AddMenu.objects.get(id=id)
    print(item)
    item.delete()
    return redirect('menu')


def edit(req, id):
    items = AddMenu.objects.get(id=id)
    if req.method == 'POST':
        item = req.POST.get('item')
        items.item=item
        items.save()
        return redirect('menu')
    return render(req, 'edit.html',{'items':items})


def register(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        username = req.POST.get('username')
        password = req.POST.get('password')
        email = req.POST.get('email')
        print(name, email,username,password)

        user = User.objects.filter(username = username)
        if user.exists():
            messages.success(req, 'Username already exist!')
            return redirect('register')

        user = User.objects.create_user(first_name = name, username=username, email=email, password=password)

         
        user.save()
        messages.success(req, 'Registered Successfully!')
        return redirect('register')
    return render(req, 'registration/register.html')


def login_page(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        usernamee = User.objects.filter(username = username)
        if not usernamee.exists():
            messages.info(req, 'Invalid username!')
            return redirect('login')

        user = authenticate(username = username, password=password)
        if user is None:
            messages.info(req, 'Invalid username or Password!')
            return redirect('login')
        
        else:
            login(req, user)
            return redirect('home')
           

    return render(req, 'registration/login.html')


def logout_page(req):
    logout(req)
    return redirect('home')