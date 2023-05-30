from django import forms
from proj.models import Category,Project, User



class RegisterProj(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = self.get_category_choices()
        self.fields['user'].choices = self.get_user_choices()

        self.fields['category'].widget.attrs['class'] = 'project-category'
        self.fields['keyword'].widget.attrs['class'] = 'project-keyword'
        self.fields['user'].widget.attrs['class'] = 'project-user'
        self.fields['function'].widget.attrs['class'] = 'project-function'

    
    category = forms.ChoiceField(choices=[])
    keyword = forms.CharField()
    user = forms.ChoiceField(choices=[])
    function = forms.CharField()

    
    class Meta:
        model = Project
        fields = ['logo', 'title', 'description', 'content']

        labels = {
            'logo': 'Logo',
            'title': 'Title',
            'description': 'Description',
            'content': 'Content',
        }
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'project-logo'}),
            'title': forms.TextInput(attrs={'class': 'project-title'}),
            'description': forms.Textarea(attrs={'class': 'project-description', 'rows': 5}),
        }


    def get_category_choices(self):
        categories = Category.objects.all()
        choices = [(category.id, category.name) for category in categories]
        return choices
    
    def get_user_choices(self):
        users = User.objects.all()
        choices = [(user.id, user.username) for user in users]
        return choices