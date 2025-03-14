from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/index.html')

def add_project(request):
    return render(request, 'admin/add_project.html')