from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from crm.forms import SignupForm, Addrecord
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have login successfully!")
            return redirect('home')
        else:
            messages.error(request, "You dont have any account !")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

    return render(request, 'home.html')


def logout_page(request):
    logout(request)
    messages.success(request, 'logout successfully!')
    return redirect('home')


def register_page(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if form.is_valid():
            form.save()
            messages.success(request, "You have registered successfully!")
            return redirect('home')
        elif password1 != password2:
            messages.error(request, "Password not matched")
            return redirect('Register')
        else:
            messages.success(request, "You have not enter correct data !")
            return redirect('Register')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def customer_detail(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You have to login to see the data')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request, 'Deleted record data successfully!')
        return redirect('home')
    else:
        messages.success(request, 'You have to login to see the data')
        return redirect('home')


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = Addrecord(request.POST or None, request.FILES or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated succesfully.....')
            return redirect('home')
        return render(request, 'update.html', {'form': form})
    else:
        messages.success(request, 'You are  not login! please login to update records')
        return redirect('home')


def add_record(request):
    form = Addrecord()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Addrecord(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added succesfully.....')
                return redirect('home')
    else:
        messages.success(request, "You must have to login to add record!")
        return redirect('home')
    return render(request, 'addrecord.html', {'form': form})
