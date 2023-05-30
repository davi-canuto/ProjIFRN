from django.urls import path
from . import views

app_name = 'user_profile'

urlpatterns = [
    path('profile/<int:user_id>/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/create/', views.login_create, name='login_create'),

]

