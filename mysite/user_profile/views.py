from django.shortcuts import render
from .models import UserProfile

def test_view(request):
    user = UserProfile.objects.get(id=1)
    return render(request, 'test.html', {'user': user})