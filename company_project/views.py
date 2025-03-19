from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from .forms import EmailForm

def profile(request):
    return render(request, 'profile.html')

def homepage(request):
    return render(request, 'homepage/index.html')

def home(request):
    return render(request, 'home.html', {'user': request.user})

@login_required(login_url='/accounts/login/')
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'admin/add_project.html', {'form': form})

@login_required(login_url='/accounts/login/')
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            # منطق إرسال البريد الإلكتروني
            return redirect('success_page')
    else:
        form = EmailForm()
    return render(request, 'send_email.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')