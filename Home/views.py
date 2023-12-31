from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments
from .forms import BookingForm
from .models import Doctors
from .form2 import ContactsForm

# Create your views here.
def index(request):

    numbers = {
         'fruits':{'Banana','Apple','Grapes'}
    }
    return render(request,'index.html',numbers)
def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form':form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contacts(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmatn.html')
    form = ContactsForm()
    dict_form= {
        'form': form
    }
    return render(request,'contacts.html',dict_form)
def departments(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)
