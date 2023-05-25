from django import forms
from proj.models import Category,Project, User
#from django.contrib.auth.models import User
#from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class RegisterProj(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = self.get_category_choices()
        self.fields['user'].choices = self.get_user_choices()

    
    category = forms.ChoiceField(choices=[])
    keyword = forms.CharField()
    user = forms.ChoiceField(choices=[])
    
    class Meta:
        model = Project
        fields = ['logo', 'title', 'description', 'content']

        labels = {
            'logo': 'Logo',
            'title': 'Title',
            'description': 'Description',
            'content': 'Content',
        }


    def get_category_choices(self):
        categories = Category.objects.all()
        choices = [(category.id, category.name) for category in categories]
        return choices
    
    def get_user_choices(self):
        users = User.objects.all()
        choices = [(user.id, user.username) for user in users]
        return choices