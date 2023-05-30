from django.shortcuts import render
from .models import UserProfile, User
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