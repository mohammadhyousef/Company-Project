from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog, name='add_blog'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
]