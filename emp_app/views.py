from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Task
from datetime import datetime

# Create your views here.
def home(request):
    if request.method == 'POST':
        uname= request.POST['uname']
        pswd= request.POST['pass']
        user= auth.authenticate(request, username=uname, password=pswd)
        if user is not None:
            auth.login(request, user=user)
            messages.success(request, ' Congrates login succesful')
            return redirect("/dashboard")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect(request, "/login")
    else:
      return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        uname= request.POST['uname']
        pswd1= request.POST['pass1']
        pswd2= request.POST['pass2']
        if pswd1 == pswd2:
              if User.objects.filter(username=uname).exists():
                 messages.error(request, 'username already exists')
                 return redirect("/signup")
              elif User.objects.filter(email=email).exists():
                 messages.error(request, 'email already exists')
                 return redirect("/signup")
              else:
               User.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=pswd1)
               messages.success(request, 'signup successful')
              return redirect("/")
        else:
             return redirect("/signup")
    messages.error(request, 'password do not match')
    return render(request, 'signup.html')

def dashboard(request):
    user = request.user
    employee = user.employee
    pending_tasks = Task.objects.filter(employee=employee, doc__isnull=True) 
    completed_tasks = Task.objects.filter(employee=employee, doc__isnull=False) 

    context = {
        'emp': employee,
        'completed': completed_tasks,
        'pending': pending_tasks,
    }
    
    return render(request, 'emp_dash.html', context)

def mark_as_completed(request, id):
    task = Task.objects.get(id=id)
    task.doc = datetime.now()
    task.save()
    print(task)
    return redirect("/dashboard")
