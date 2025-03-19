from django.urls import path 
from projects.views import project_list, add_project
from blog.views import blog_list
from newsletter.views import subscribe, send_email_view
from accounts.views import user_login, user_logout

urlpatterns = [
    path('projects/', project_list, name='project_list'),
    path('projects/add/', add_project, name='add_project'),
    path('blog/', blog_list, name='blog_list'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send_email/', send_email_view, name='send_email'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]