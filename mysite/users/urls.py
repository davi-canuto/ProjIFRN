from django.urls import path
from .views import UsersView

app_name = 'users'

urlpatterns = [
    path('profile/<int:user_id>/', UsersView.profile_view, name='profile'),
    path('login/', UsersView.login_view, name='login'),
    path('logout/', UsersView.logout_view, name='logout'),
    path('login/create/', UsersView.login_create, name='login_create'),

]

