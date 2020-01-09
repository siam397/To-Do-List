from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from .models import todoitem

# Create your views here.


def todo(request):
    items=todoitem.objects.all()
    return render(request,"todolist.html",{'items':items})


def addtodo(request):
    if request.method == 'POST':
        newitem = todoitem(content=request.POST['content'])
        newitem.save()
        return HttpResponseRedirect('/')

    else:
        return render(request,'todolist.html')


def deletetodo(request,todolist_id):
        itemDel = todoitem.objects.get(id=todolist_id)
        itemDel.delete()
        return HttpResponseRedirect('/')

