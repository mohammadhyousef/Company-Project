from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Blog
from blog.forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})



def delete_blog(request, blog_id):
    project = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        project.delete()
        return redirect('blog_list')
    return render(request, 'blog/blog_list.html')