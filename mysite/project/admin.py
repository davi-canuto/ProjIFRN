from django.contrib import admin
from .models import Category, Function, Involvement, Project, Keyword
from django_summernote.admin import SummernoteModelAdmin

class ProjectAdim(SummernoteModelAdmin):
    summernote_fields = ('content')

admin.site.register(Category)
admin.site.register(Function)
admin.site.register(Involvement)
admin.site.register(Project)
admin.site.register(Keyword)

