from email import message
from os import name
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import *


def Home(request):
    viewData=CrudOperation.objects.all()
    return render (request,'view.html',{'views':viewData})

def Add(request):
    if request.method=='POST':
        name= request.POST['name']
        mobile= request.POST['mobile']
        CrudOperation(name=name,mobile=mobile).save()

        messages.success(request,'Data Added Successfully')
        return redirect('')
    else:
        messages.warning(request,'Something Went Wrong')
    return render (request,'add.html')


def Edit(request,id):
    gotData = CrudOperation.objects.get(id=id)

    if request.method == 'POST':
        id=gotData.id 
        name=request.POST['name']
        mobile=request.POST['mobile']
        CrudOperation(id=id,name=name,mobile=mobile).save()
        return redirect('')
    return render (request,'edit.html',{'data':gotData})

def DeleteData(request,id):
    gotData=CrudOperation.objects.get(id=id)
    gotData.delete()
    return redirect('')