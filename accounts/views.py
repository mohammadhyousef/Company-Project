from django.contrib.auth import login, logout, authenticate 
from django.shortcuts import render, redirect 

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('project_list')
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
