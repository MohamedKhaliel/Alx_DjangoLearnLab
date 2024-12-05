from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .forms import SignUpForm , LoginForm , ProfileForm

# Create your views here.

def home(request):
    return render(request , 'blog/base.html')

def register(request):
    if request.method == "POST" :
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , 'registered successfully')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request , 'blog/register.html' , {'form':form})

def login_view(request):
    if request.method == 'Post' :
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request , user)
                return redirect('')
            else:
                messages.error(request , 'invalid credentials')
                return redirect('')
    else:
        form = LoginForm()
    return render(request , 'blog/login.html' , {'form':form})

def logout_view(request):
    logout(request)
    messages.success(request , "Logged out successfully!")
    return redirect('login')


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST , instance = user)
        if form.is_valid():
            form.save()
            messages.success(request , 'profile updated successfully')
            return redirect('profile')
    else:
        form = ProfileForm(instance = user)
    return render(request , 'blog/profile.html' , {'form':form})