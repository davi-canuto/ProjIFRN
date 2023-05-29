from django.urls import path
from . import views

app_name = 'proj'

urlpatterns = [
    path('register/', views.register_project, name='register'),
    path('create/', views.create_project, name='create'),


]