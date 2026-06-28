from django.shortcuts import render,redirect
from django.contrib.auth import logout as auth_logout,login as auth_login,authenticate
from django.contrib.auth.models import User

# Create your views here.
def login(request):
        if request.method=='POST':#if user use the input field
            username=request.POST['username']#assigning the input values into a variable
            password=request.POST['password']
            print(username,password)
            u=authenticate(username=username,password=password)
            print(u)
            if u:
                auth_login(request,u)
                return redirect('home')
            else:
                return render(request,'login.html',{'error':'invalid username or password'})
        return render(request,'login.html')
    

def logout(request):
    auth_logout(request)
    return redirect('login')
    


def register(request):
     if request.method=='POST':
        print('successfully posted')
        try:
            print('checking username')
            u=User.objects.get(username=request.POST['username'])
            return render(request,'register.html',{'error':'username is already exist//please try a unique user name'})
        except:
             print('creating user')
             if request.method=='POST':
                  #we have to get the exact values those are present in users_auth default model in db
                  first_name=request.POST['first_name']
                  last_name=request.POST['last_name']
                  username=request.POST['username']
                  email=request.POST['email']
                  u=User.objects.create(username=username,email=email,first_name=first_name,last_name=last_name)#here u variable will be used instead of User ,cause we have to access the values from the form not from the database
                  print('user created successfully')
                  u.set_password(request.POST['password'])
                  u.save()
                  print('password set successfully')
                  return redirect('login')
             return render(request,'register.html')
        
     return render(request,'register.html')