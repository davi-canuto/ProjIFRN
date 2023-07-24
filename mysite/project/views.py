from django.shortcuts import render, redirect
from django.http import Http404
from .forms import RegisterProj
from .models import *
from django.contrib.auth.decorators import login_required
import pdb


def homeProject(request):
    projects = Project.objects.all().order_by('-id')
    length_fin = projects.filter(status='finalizado').__len__
    length_and = projects.filter(status='em_andamento').__len__

    context = {
        'projects': projects,
        'status_choices': STATUS_CHOICES,
        'length_fin': length_fin,
        'length_and': length_and,
    }
    
    return render(
        request,
        'project/pages/home.html',
        context,
    )

class ProjectView:
    def detailProject(request, project_id):
        project = Project.objects.get(id=project_id)
        context = {'project':project}
        return render(
            request,
            'project/pages/detail_project.html',
            context,
        )

    @login_required(login_url='users:login', redirect_field_name='next')
    def registerProject(request):
        form = RegisterProj()
        return render(
            request,
            'project/pages/register_project.html',
            {'form': form, }         
        )


    def saveProject(request):
        if request.method != 'POST':
            raise Http404
        
        form2 = request.POST
        form = RegisterProj(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)

            # Category
            project.category = CategoryView.searchCategory(request)

            project.save()
            # Keyword
            
            keyword = KeywordView.searchKeyword(request)
            if keyword == None:
                keyword = KeywordView.saveKeyword(request)
            project.keyword.add(keyword)

            # Logo
            if 'logo' in request.FILES:
                project.logo = request.FILES['logo']
            
            # function
            function = FunctionView.searchFunction(request)
            if function == None:
                function = FunctionView.saveFunction(request)


            # Involvement
            InvolvementView.saveInvolvement(request, project, function)    
        
            return redirect('project:register')

        form = RegisterProj()
        return redirect('project:register')
 


class CategoryView:
    @staticmethod
    def searchCategory(request):
        category_id = request.POST['category']
        category = Category.objects.filter(id=category_id).first()
        return category
    

class KeywordView:
    @staticmethod
    def searchKeyword(request):
        keyword_name = request.POST['keyword'].lower()
        keyword = Keyword.objects.filter(name=keyword_name).first()
        return keyword
    
    @staticmethod
    def saveKeyword(request):
        keyword_name = request.POST['keyword'].lower()
        return Keyword.objects.create(name=keyword_name)
    

class InvolvementView:
    @staticmethod
    def saveInvolvement(request, project, function):
        user_id = request.POST['user']
        user = User.objects.get(id=user_id)
        involvement = Involvement.objects.create(user=user, project=project, function=function)
        return involvement
    

class FunctionView:
    @staticmethod
    def searchFunction(request):
        function_name = request.POST['function'].lower()
        function = Function.objects.filter(name=function_name).first()
        return function
    
    @staticmethod
    def saveFunction(request):
        function_name = request.POST['function'].lower()
        return Function.objects.create(name=function_name)