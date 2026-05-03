"""
URL configuration for the projects app.
Routes for the portfolio website.
"""
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_list, name='projects_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
]
