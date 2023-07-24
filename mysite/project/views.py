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

        previous_url = request.META.get('HTTP_REFERER')        
        #pdb.set_trace()

        project = Project(
            logo = request.FILES['logo'],
            title = request.POST['title'],
            description = request.POST['description'],
            content = request.POST['content'],
        )

        # Category
        project.category = CategoryView.searchCategory(request)

        # Keyword
        project.save()
        keywords = request.POST.getlist('keyword')
        for key in keywords:
            keyword = KeywordView.searchKeyword(key)
            if keyword == None:
                keyword = KeywordView.saveKeyword(key)
            project.keyword.add(keyword)


        # Involvement do gerente
        gerente_id = request.user.id
        gerente = User.objects.get(id=gerente_id)
        invol = Involvement(project=project, user=gerente, is_manager=True)
        invol.save()


        # Involvement
        users_and_function = request.POST.getlist('user_and_function')
        for string_full in users_and_function:
            string_break = string_full.split('-')
            username = string_break[0]
            function_name = string_break[1]
            function = FunctionView.saveFunction(function_name)
            if function == None:
                keyword = KeywordView.saveKeyword(function_name)
            InvolvementView.saveInvolvement(project, function, username)    
    
        if previous_url:
            return redirect(previous_url)
        else:
            return redirect('fallback_url_name')

    
    def deleteProject(request, project_id):
        project = Project.objects.get(id=project_id)
        previous_url = request.META.get('HTTP_REFERER')
        project.delete()

        if previous_url:
            return redirect(previous_url)
        else:
            return redirect('fallback_url_name')

 


class CategoryView:
    @staticmethod
    def searchCategory(request):
        category_id = request.POST['category']
        category = Category.objects.filter(id=category_id).first()
        return category
    

class KeywordView:
    @staticmethod
    def searchKeyword(key):
        keyword_name = key.lower()
        keyword = Keyword.objects.filter(name=keyword_name).first()
        return keyword
    
    @staticmethod
    def saveKeyword(key):
        keyword_name = key.lower()
        return Keyword.objects.create(name=keyword_name)
    

class InvolvementView:
    @staticmethod
    def saveInvolvement(project, function, username):
        user = User.objects.get(username=username)
        involvement = Involvement.objects.create(user=user, project=project, function=function)
        return involvement
    

class FunctionView:
    @staticmethod
    def searchFunction(function_name):
        function = function_name.lower()
        function_obj = Function.objects.filter(name=function).first()
        return function_obj
    
    @staticmethod
    def saveFunction(function_name):
        function = function_name.lower()
        return Function.objects.create(name=function)