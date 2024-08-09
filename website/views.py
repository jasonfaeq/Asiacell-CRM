from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm


# Define the home view
def home(request): 
    records = Record.objects.all() # Get all records from the database
    
    # POST request
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"] 
        user = authenticate(request, username=username, password=password) # Authenticate the user with the given username and password
        if user is not None: 
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "home.html", {'records': records}) # Render the home.html template with the records

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('home')

def customer_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk) # Get the record with the given id
        return render(request, "record.html", {'record': record}) # Render the record.html template with the record
    else:
        messages.error(request, "You need to login first.")
        return redirect('home')

def delete_customer(request, pk):
    if request.user.is_authenticated:
        deleteIt = Record.objects.get(id=pk) # Get the record with the given id
        deleteIt.delete() # Delete the record
        messages.success(request, "Record deleted successfully.")
        return redirect('home')
    else:
        messages.error(request, "You need to login first.")
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                record = form.save(commit=False)
                record.user = request.user
                record.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        return render(request, "add_record.html", {'form': form})
    else: 
        messages.error(request, "You need to login first.")
        return redirect('home')

def update_record(request, pk):
    record = Record.objects.get(id=pk) # Get the record with the given id
    form = AddRecordForm(request.POST or None, instance=record)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record updated successfully.")
                return redirect('home')
        return render(request, "update_record.html", {'form': form})
    else:
        messages.error(request, "You need to login first.")
        return redirect('home')