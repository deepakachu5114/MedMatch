from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Doctors
from .forms import UserRegistrationForm
from .forms import DoctorsForm

# Create your views here.


def index(response):
    return render(response, 'doctors/index.html')


def home(response):
    pass

def register_user(response):

    form = UserRegistrationForm()
    if response.method == 'POST':
        form = UserRegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')
    else:
        form = UserRegistrationForm()

    context = {'registerForm': form}

    return render(response, 'doctors/register_user.html', context=context)


def register_doctor(request):
    if request.method == 'POST':
        form = DoctorsForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other desired view
            return redirect('my-login')  # Change 'success_url_name' to the actual URL name
    else:
        form = DoctorsForm()

    return render(request, 'doctors/'
                           'register_doctor.html', {'form': form})

def login(response):
    return render(response, 'doctors/my-login.html')


def logout(response):
    pass


def dashboard(response):
    return render(response, 'doctors/dashboard.html')
