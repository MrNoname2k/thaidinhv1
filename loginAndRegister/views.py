from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse as response


# Create your views here.
@csrf_exempt
def goLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password =password  )
        print(f'login with {user.username} and {user.password}')
        if user is not None:
            auth.login(request , user)
            return redirect('/home')   
        else:
            messages.info(request, 'invalid username or password')
            return response('invalid username or password')
    else:
        return render(request,'loginAndRegister/login.html')

@csrf_exempt
def goRegister(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            username = request.POST['username']
            password= request.POST['password']
            first_name = request.POST['firstName']
            last_name= request.POST['lastName']
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print(f'{user.id} đã được đăng ký với username{user.username}')
            return redirect('/login')
        except:
            message = 'Thông tin điền vào không đúng định dạng'
            return redirect('/register')
            
        
    return render(request, 'loginAndRegister/register.html')
