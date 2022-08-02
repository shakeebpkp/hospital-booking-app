from django.http import HttpResponse
from django.shortcuts import render
from .models import Departments, Doctors
from .forms import BookingForm, ContactForm

# Create your views here.

def index(request):
    doc=Doctors.objects.all()
    return render(request, 'index.html',{'doctors':doc})

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    return render(request, 'booking.html',{'form':form})

def doctors(request):
    doc=Doctors.objects.all()
    return render(request, 'doctors.html',{'doctors':doc})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'contact.html')

def department(request):
    dept=Departments.objects.all()
    return render(request, 'department.html',{'departments':dept})