from django.shortcuts import render,redirect
from . models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')#login_url is used to navigate the user to the login page

def home(request):
    data = FlightDetails.objects.all()

    to= request.GET.get("To")    
    fro = request.GET.get("from")     
    if to and fro:
        data = data.filter( From__iexact=to,To__iexact=fro)
        
    return render (request,'home.html',{'data':data})

@login_required(login_url='login')
def booking(request):
    now=Book_Details.objects.all().order_by ("-id")
    return render (request,'booking.html',{"now":now})

@login_required(login_url='login')
def history(request):

    return render (request,'history.html')

@login_required(login_url='login')
def profile(request):
    
    return render (request,'profile.html',{'data':request.user})

@login_required(login_url='login')
def support(request):
    
    return render (request,'support.html')

def about(request):
    
    return render (request,'about.html')

@login_required(login_url='login')
def book(request ,id):
    data=FlightDetails.objects.get(id=id)
    if request.method=='POST':
        Book_Details.objects.create(
            model=data.model,
            name=data.name,
            no=data.no,
            From=data.From,
            To=data.To,
            Departure=data.Departure,
            Date=data.Date,
            Price=data.Price,
            your_name=request.POST.get('your_name'),
            Email=request.POST.get('Email'),
            Phone_no=request.POST.get('Phone_no'),
            Adhaar_no=request.POST.get('Adhaar_no'),
            age=request.POST.get('age'),
            seat_class=request.POST.get('seat_class'),
            seat_no=request.POST.get('seat_no')
        )

        return redirect('success')

    return render(request, 'book.html', {'data': data})

@login_required(login_url='login')
def update(request,id):
    b=Book_Details.objects.get(id=id)
    if request.method=='POST':
        b.your_name=request.POST.get('your_name')
        b.Phone_no=request.POST.get('Phone_no')
        b.seat_class=request.POST.get('seat_class')
        b.save()
        return redirect('booking')
    return render(request,'update.html',{'b':b})

@login_required(login_url='login')
def clear(request,id):
    a=Book_Details.objects.get(id=id)
    a.delete()
    return redirect('home')

@login_required(login_url='login')
def success(request):
    return render(request,'success.html')
 