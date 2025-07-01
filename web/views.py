from django.shortcuts import get_object_or_404, render,redirect
from.models import fees, student,category,product,contact
from django.db.models import Q,Sum,F
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json


# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        errors = []

        # Validation
        if not username or not email or not password or not confirm_password:
            errors.append("All fields are required!")
        if password != confirm_password:
            errors.append("Passwords do not match!")
        if User.objects.filter(username=username).exists():
            errors.append("Username already exists!")

        if errors:
            return JsonResponse({"success": False, "errors": errors})

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        return JsonResponse({"success": True})

    return render(request, "register.html")

# User Login (Without Forms)
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "errors": "Invalid username or password!"})

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('login_view')


def about(request):
    return render(request,"about.html")

def contact1(request):
    return render(request,"contact1.html")

def base(request):
    return render(request,"base.html")

def index(request):
    posts=student.objects.all()
    return render(request,'index.html',{'posts': posts})

def showstudent(request):
    s = student.objects.annotate(
        total_fees_paid=Sum('fees__payment'),
        remaining_fees= F('amount') - Sum('fees__payment')
    )
    stu= student.objects.all()
    return render(request,'showstudent.html',{'student':stu,'student':s})

@login_required(login_url='login_view')    
def showstudentlist(request):
    # query = request.GET.get('q')
    # search = request.GET.get('search')

    # if query == 'city':
    #     stu = student.objects.filter(city=search)
    # elif query == 'fname':
    #     stu = student.objects.filter(fname__icontains=search)
    # elif query == 'lname':
    #     stu = student.objects.filter(lname__icontains=search)
    # elif query == 'gender' :
    #     stu = student.objects.filter(gender=search)         
    # else:    
    
        
    s = student.objects.annotate(
        total_fees_paid=Sum('fees__payment'),
        remaining_fees= F('amount') - Sum('fees__payment')
    )
    stu= student.objects.all()
    return render(request,'showstudentlist.html',{'student':stu,'student':s})


def showcategorylist(request):
    cat= category.objects.all()
    return render(request,'showcategorylist.html',{'category':cat})

def showproductlist(request):
    
    query = request.GET.get('q')
    q1 = request.GET.get('q1')
    if query and q1:
        pro = product.objects.filter(stock__gt=query,stock__lt=q1)     
    else:    
        pro= product.objects.all()
    return render(request,'showproductlist.html',{'product':pro,'que':query,'q1':q1})

def showcontactlist(request):
    print("fasdfasf")
    query = request.GET.get('q')
    q2 = request.GET.get('q2')
    if query and q2:
        cn = contact.objects.filter(address=query,email=q2)    
    else:    
        cn= contact.objects.all().order_by('-address')
    return render(request,'showcontactlist.html',{'contact':cn,'que':query,'q2':q2})   

@login_required(login_url='login_view')
def showfeeslist(request):
    # Get the date range from the request
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')

    f = fees.objects.all()
    #print(posts)
    # Filter based on the date range if provided
    if from_date and to_date:
        f = fees.objects.filter(date_paid__range=[from_date, to_date])
    elif from_date:  # Filter from a specific date
        f = fees.objects.filter(date_paid__gte=from_date)
    elif to_date:  # Filter up to a specific date
        f = fees.objects.filter(date_paid__lte=to_date)

    
    return render(request, 'showfeeslist.html', {'lalo': f, 'from_date': from_date, 'to_date': to_date})

@login_required(login_url='login_view')
def addstudent(request):
    if request.method == "POST":
        s = student()
        s.fname  = request.POST.get('txtfname')
        s.lname = request.POST.get('txtlname')
        s.rno =  request.POST.get('txtrno')
        s.std = request.POST.get('txtstd')
        s.gender= request.POST.get('txtgender')
        s.city= request.POST.get('txtcity')
        s.amount= request.POST.get('txtamount')
        s.image = request.FILES.get('txtimage')
        s.courses = request.POST.get('txtcourses')
        s.save()
        return redirect('showstudentlist')
        
    else:
        return render(request,"addstudent.html")
    
def addproduct(request):
    if request.method == "POST":
        s = product()
        s.name  = request.POST.get('txtname') 
        s.description = request.POST.get('txtdescription')
        s.stock =  request.POST.get('txtstock')
        s.price = request.POST.get('txtprice')
        s.image = request.FILES.get('txtimage')
        s.save()
        return redirect(showproductlist)
        
    else:
        return render(request,"addproduct.html")
    
def addcontact(request):
    if request.method == "POST":
        c = contact()
        c.fname  = request.POST.get('txtfname') 
        c.lname = request.POST.get('txtlname')
        c.email =  request.POST.get('txtemail')
        c.group = request.POST.get('txtgroup')
        c.address= request.POST.get('txtaddress')
        c.birth= request.POST.get('txtbirth')
        c.image = request.FILES.get('txtimage')
        c.save()
        return redirect(showcontactlist)
        
    else:
        return render(request,"addcontact.html")

@login_required(login_url='login_view')
def addfees(request):
    if request.method == "POST":
        f = fees() 
        sa= request.POST.get('student')
        students = get_object_or_404(student, pk=sa)
        f.student=students
        f.payment=request.POST.get('payment')
        f.date_paid=request.POST.get('date_paid')
        f.take=request.POST.get('take')
        f.pay_method=request.POST.get('pay_method')
        f.save()
        return redirect(showfeeslist) 
    
    else:
        students = student.objects.all() 
        return render(request,'addfees.html',{'s':students})
    


def delete_contact(request,id):
    c = contact.objects.get(id = id)

    c.delete()
    return redirect(showcontactlist)

@login_required(login_url='login_view')
def delete_student(request,id):
    s = student.objects.get(id = id)
    s.delete()
    return redirect(showstudentlist)

def delete_product(request,id):
    p = product.objects.get(id = id)
    p.delete()
    return redirect(showproductlist)

@login_required(login_url='login_view')
def delete_fees(request,id):
    f = fees.objects.get(id = id)
    f.delete()
    return redirect(showfeeslist)

def edit_contact(request,id):
    s = contact.objects.get(id=id)
    if request.method == "POST":
        s.fname  = request.POST.get('txtfname') 
        s.lname = request.POST.get('txtlname')
        s.email =  request.POST.get('txtemail')
        s.group = request.POST.get('txtgroup')
        s.address= request.POST.get('txtaddress')
        s.birth= request.POST.get('txtbirth')
        s.image = request.FILES.get('txtimage')
        s.save()
        return redirect(showcontactlist)
        
    else:
        return render(request,"addedit.html",{"contact" : s})

@login_required(login_url='login_view')
def edited_student(request,id):
    c = student.objects.get(id=id)
    if request.method == "POST":
        c.fname  = request.POST.get('txtfname') 
        c.lname = request.POST.get('txtlname')
        c.rno =  request.POST.get('txtrno')
        c.std = request.POST.get('txtstd')
        c.gender= request.POST.get('txtgender')
        c.city= request.POST.get('txtcity')
        c.amount= request.POST.get('txtamount')
        c.image = request.FILES.get('txtimage')
        c.courses = request.POST.get('txtcourses')
        c.save()
        return redirect(showstudentlist)
        
    else:
        return render(request,"addedited.html",{"student" : c})

def editted_product(request,id):
    s = product.objects.get(id=id)
    if request.method == "POST":
        s.name  = request.POST.get('txtname') 
        s.description= request.POST.get('txtdescription')
        s.price =  request.POST.get('txtprice')
        s.stock = request.POST.get('txtstock')
        s.review = request.POST.get('txtreview')
        s.image = request.FILES.get('txtimage')
        s.save()
        return redirect(showproductlist)
        
    else:
        return render(request,"addeditted.html",{"product" : s})


# def studentdetail(request,id):
#     s= student.objects.get(student,id)
#     return render(request,"studentdetail.html",{"s": student})

@login_required(login_url='login_view')
def studentdetail(request,id):
    s = get_object_or_404(student, id=id)
    payment=fees.objects.filter(student=s)

    return render(request, "studentdetail.html", {'student':s,'payment':payment})
