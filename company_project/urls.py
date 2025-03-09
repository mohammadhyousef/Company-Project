"""
URL configuration for company_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from projects.views import project_list, add_project
from blog.views import blog_list
from accounts.views import user_login, user_logout
from newsletter.views import subscribe, send_email_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', project_list, name='project_list'),
    path('projects/add/', add_project, name='add_project'),
    path('blog/', blog_list, name='blog_list'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send_email/', send_email_view, name='send_email'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
 
]
