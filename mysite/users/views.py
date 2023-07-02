from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
import pdb


class UserView:
    def profileUser(request, user_id):
        user = User.objects.get(id=user_id)
        involvements = user.involvement_set.all()
        
        context = {'user': user, 'involvements': involvements}

        #pdb.set_trace()

        return render(
            request,
            'users/pages/profile.html',
            context,
        )


    def loginUser(request):
        form = LoginForm()
        return render(
            request,
            'users/pages/login.html',
            {'form': form},
        )


    def authenticateUser(request):
        if request.method != 'POST':
            raise Http404

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username', '')
            password = form.cleaned_data.get('password', '')
            authenticate_user = authenticate(username=username, password=password)
            if authenticate_user is not None:
                login(request, authenticate_user)
                return redirect('project:home')
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('users:login')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('users:login')
        

    @login_required(login_url='users:login', redirect_field_name='next')
    def logoutUser(request):
        logout(request)
        return redirect('project:home')