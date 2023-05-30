from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
import pdb

def profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    involvements = user.involvement_set.all()
    
    context = {'user': user, 'involvements': involvements}

    #pdb.set_trace()

    return render(
        request,
        'user_profile/pages/profile.html',
        context,
    )


def login_view(request):
    form = LoginForm()
    return render(
        request,
        'user_profile/pages/login.html',
        {'form': form},
    )


def login_create(request):
    if request.method != 'POST':
        raise Http404

    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data.get('username', '')
        password = form.cleaned_data.get('password', '')
        authenticate_user = authenticate(username=username, password=password)
        if authenticate_user is not None:
            messages.success(request, 'Successs')
            login(request, authenticate_user)
            return redirect('proj:home')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('user_profile:login')
    else:
        messages.error(request, 'Invalid username or password')
        return redirect('user_profile:login')
    

@login_required(login_url='user_profile:login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    return redirect('proj:home')