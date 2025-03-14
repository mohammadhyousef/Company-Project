from django.shortcuts import render

def blog_list(request):
    # منطق عرض المدونة هنا
    return render(request, 'blog/blog_list.html')