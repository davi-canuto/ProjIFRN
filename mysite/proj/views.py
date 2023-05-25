from django.shortcuts import render, redirect
from .forms import RegisterProj
from .models import Category
import pdb


def register_project(request):
    form = RegisterProj()
    return render(
        request,
        'testeForm.html',
        {'form': form, }         
    )


def create_project(request):
    if request.method == 'POST':
        form = RegisterProj(request.POST, request.FILES)

        if form.is_valid():
            category_id = form.cleaned_data['category']
            # user_id = form.cleaned_data['user']
            # logo = form.cleaned_data['logo']

            category = Category.objects.get(id=category_id)
            # user = User.objects.get(id=user_id)
            
            project = form.save(commit=False)
            project.category = category

            if 'logo' in request.FILES:
                project.logo = request.FILES['logo']

            project.save()
            return redirect('proj:register')

        form = RegisterProj()
        return redirect('proj:register')
 

def register_img(request):
    return render(
        request,
        'sendimg.html',
    )

def create_img(request):
    if request.method == 'POST':
        img = request.FILES['img']

    pdb.set_trace() 
    return redirect('proj:registerimg')