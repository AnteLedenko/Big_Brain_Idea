from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, ProfileUpdateForm
from blog.models import Post 
from django.http import JsonResponse
import os

def health_check(request):
    required_vars = [
        'SECRET_KEY',
        'DATABASE_URL',
        'EMAIL_HOST_USER',
        'EMAIL_HOST_PASSWORD',
        'DJANGO_SUPERUSER_USERNAME',
        'DJANGO_SUPERUSER_EMAIL',
        'DJANGO_SUPERUSER_PASSWORD',
    ]
    env_status = {var: os.getenv(var, 'MISSING') for var in required_vars}
    return JsonResponse(env_status)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', username=user.username )
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile', username=user.username)
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'users/logout.html') 

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-date_posted') 
    return render(request, 'users/profile.html', {'user_profile': user, 'posts': posts})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/update_profile.html', {'form': form})
