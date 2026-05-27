from django.shortcuts import render,redirect
from testapp.models import Employee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms  import SignupForm, LoginForm



# Create your views here.
@login_required
def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'index_r.html',{'emp_list':emp_list})

#To insert the data
from testapp.forms import EmployeeForm
@login_required
def insert_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')   # ✅ moved INSIDE if form.is_valid()
    return render(request, 'insert.html', {'form': form})
    #delete
@login_required
def delete_view(request,id):
        emp = Employee.objects.get(id=id)
        emp.delete()
        return redirect('/')

#update
@login_required
def update_view(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})


# ─── Auth Views ───────────────────────────────────────────────
#signup view

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('retrive_view')

    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # hash the password
        user.save()
        messages.success(request, "Account created! Please log in.")
        return redirect('login')

    return render(request, 'signup.html', {'form': form})

#Login in View

def login_view(request):
    if request.user.is_authenticated:
        return redirect('retrive_view')

    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('retrive_view')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html', {'form': form})

#Logout View
def logout_view(request):
    logout(request)
    return redirect('login')





