from django.urls import path
from .views import UserView

app_name = 'users'

urlpatterns = [
    path('profile/<int:user_id>/', UserView.profileUser, name='profile'),
    path('login/', UserView.loginUser, name='login'),
    path('logout/', UserView.logoutUser, name='logout'),
    path('login/create/', UserView.authenticateUser, name='authenticate'),

]

