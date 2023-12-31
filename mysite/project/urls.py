from django.urls import path
from .views import ProjectView, homeProject

app_name = 'project'

urlpatterns = [
    path('', homeProject, name='home'),
    path('project/detail/<int:project_id>/', ProjectView.detailProject, name='detail'),
    path('project/register/', ProjectView.registerProject, name='register'),
    path('project/create/', ProjectView.saveProject, name='create'),
    path('project/delete/<int:project_id>/', ProjectView.deleteProject, name='delete'),

]
