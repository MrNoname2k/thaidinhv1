from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Item
from django.http import HttpResponse as response

# Create your views here.
def goHome(request):
    items = Item.objects.all()
    context = {'items': items}
    customer = None
    if(request.user.is_authenticated):
        customer = request.user
    print(f'Người dùng đăng nhập vào {customer}')
    return render(request,'shop/_home.html',context)

def logout(request):
    auth.logout(request)
    return redirect('/home')

def getItem(request,id):
    items = Item.objects.all()
    detail = Item.objects.get(id=id)
    context ={'items':items,'detail':detail}
    return render(request,'shop/_item_detail.html',context)
