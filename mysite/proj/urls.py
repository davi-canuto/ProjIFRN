from django.urls import path
from . import views

app_name = 'proj'

urlpatterns = [
    path('', views.home_project, name='home'),
    path('project/detail/<int:project_id>', views.detail_project, name='detail'),
    path('project/register/', views.register_project, name='register'),
    path('project/create/', views.create_project, name='create'),


]
