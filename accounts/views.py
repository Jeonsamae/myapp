from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home_view(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    # if request.method == 'POST':
    #     form = CustomAuthenticationForm(request, data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('content')
    # else:
    #     form = CustomAuthenticationForm()
    # return render(request, 'login.html', {'form': form})
    pass

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def content_view(request):
    return render(request, 'content.html')
