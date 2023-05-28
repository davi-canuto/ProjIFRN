from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterProj
from .models import Category, User,Involvement, Keyword, Function
import pdb


def register_project(request):
    form = RegisterProj()
    return render(
        request,
        'testeForm.html',
        {'form': form, }         
    )


def create_project(request):
    if request.method != 'POST':
        raise Http404
    
    form = RegisterProj(request.POST, request.FILES)

    if form.is_valid():
        project = form.save(commit=False)

        # Category
        category_id = form.cleaned_data['category']
        category = Category.objects.get(id=category_id)
        project.category = category

        # User
        user_id = form.cleaned_data['user']
        user = User.objects.get(id=user_id)

        # Keyword
        project.save()
        keyword_list = form.cleaned_data['keyword'].split(',')
        for k in keyword_list:
            try:
                k = k.strip().lower()
                keyword = Keyword.objects.get(name=k)
            except Keyword.DoesNotExist:
                keyword = None

            if keyword == None:
                keyword = Keyword()
                keyword.name = k
                keyword.save()
                project.keyword.add(keyword)
            
        # Logo
        if 'logo' in request.FILES:
            project.logo = request.FILES['logo']
        
        project.save()

        # Involvement
        invol = Involvement()
        invol.project = project
        invol.user = user
        invol.save()

        # function
        function = Function()
        function_name = form.cleaned_data['function']
        function.name = function_name
        function.involt = invol
        function.save()

        return redirect('proj:register')

    form = RegisterProj()
    return redirect('proj:register')
 
# form.cleaned_data