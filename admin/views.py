from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import ProjectForm

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProjectForm()
    return render(request, 'admin/add_project.html', {'form': form})