from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from project_app.models import Project
from task_app.models import Task

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'user_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_app/register.html'
    success_url = reverse_lazy('login')

@login_required
def dashboard(request):
    user = request.user
    projects = user.created_projects.all()
    tasks = user.assigned_tasks.all()
    context = {
        'user': user,
        'projects': projects,
        'tasks': tasks,
    }
    return render(request, 'user_app/dashboard.html', context)

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'user_app/home.html')
