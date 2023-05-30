from django.urls import path
from . import views

app_name = 'proj'

urlpatterns = [
    path('home/', views.home_project, name='home'),
    path('detail/<int:project_id>', views.detail_project, name='detail'),
    path('register/', views.register_project, name='register'),
    path('create/', views.create_project, name='create'),


]
