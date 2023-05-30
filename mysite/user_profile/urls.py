from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('<int:user_id>/', views.profile_view, name='profile')
]

