from django.contrib import admin
from django.urls import path
from projects.views import project_list, add_project
from blog.views import blog_list
from newsletter.views import subscribe, send_email_view
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', project_list, name='project_list'),  # المسار الصحيح لعرض قائمة المشاريع
    path('projects/add/', add_project, name='add_project'),
    path('blog/', blog_list, name='blog_list'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send_email/', send_email_view, name='send_email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
urlpatterns += i18n_patterns(
    path('', views.homepage, name='homepage'),
    path('admin/add-project/', views.add_project, name='add_project'),
)