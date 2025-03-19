from django.contrib import admin
from django.urls import path, include
from projects.views import project_list, add_project, delete_project
from blog.views import blog_list
from newsletter.views import subscribe, send_email_view
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('', project_list, name='project_list'),  
    path('admin/', admin.site.urls),
    path('projects/', project_list, name='project_list'),  
    path('projects/add/', add_project, name='add_project'),
    path('projects/delete/<int:project_id>/', delete_project, name='delete_project'),
    path('blog/', include('blog.urls')),  
    path('subscribe/', subscribe, name='subscribe'),
    path('send-email/', views.send_email, name='send_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),  
    path('accounts/login/', views.login_view, name='login'),
    path('i18n/', include('django.conf.urls.i18n')), 
]

urlpatterns += i18n_patterns(
    path('', views.homepage, name='homepage'),
    path('admin/add-project/', views.add_project, name='add_project'),
)