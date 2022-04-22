from django.shortcuts import render
from django.http import HttpResponseRedirect
from  django.http import HttpResponse
from . import forms,models
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.core.mail import send_mail

# Create your views here.


def  Home(request) :
	context={}
	return render(request,"home.html",context)
def Admin(request):
	context={}
	return render(request,"admin.html",context)
def Student(request):
	context={}
	return render(request,"student.html",context)

def adminsignup_view(request):
    form=forms.AdminSigupForm
    context={'form':form}
    if request.method=='POST':
        form=forms.AdminSigupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()


            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            
            return render(request,'adminsignup.html',context)
    return render(request,'adminsignup.html',context)

def adminsignin_view(request):
	return HttpResponseRedirect('admin')

def addbook_view(request):
    #now it is empty book form for sending to html
    form=forms.BookForm
    context={'form':form}
    if request.method=='POST':
        #now this form have data from html
        form=forms.BookForm(request.POST)
        if form.is_valid():
            user=form.save()
            return render(request,'addbook.html',context)
    return render(request,'addbook.html',context)

from .models import Book
def  BookView(request) :
    context={'librarydb':Book.objects.all()}
    return render(request,'bookview.html',context)

def adminclick_view(request):
    context={}
    return render(request,'adminsignin.html',context)















