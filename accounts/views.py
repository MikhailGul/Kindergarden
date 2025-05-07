from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm
from children.models import Child
from django.contrib.auth import logout as auth_logout

def home(request):
    return render(request, 'home.html')

def logout(request):
    auth_logout(request)
    return redirect('home')  # Перенаправление на главную страницу после выхода

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Неверные учетные данные'})
    return render(request, 'accounts/login.html')


@login_required
def profile(request):
    children = request.user.child_set.filter(status='approved')
    return render(request, 'accounts/profile.html', {'children': children})