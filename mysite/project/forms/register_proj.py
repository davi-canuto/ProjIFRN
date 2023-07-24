from django import forms
from project.models import Category,Project, User



class RegisterProj(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].choices = self.get_category_choices()
        self.fields['user'].choices = self.get_user_choices()

        self.fields['category'].widget.attrs['class'] = ''
        self.fields['keyword'].widget.attrs['class'] = 'project-keyword'
        self.fields['user'].widget.attrs['class'] = 'user_choice'
        self.fields['function'].widget.attrs['class'] = ''

        self.fields['user'].widget.attrs['id'] = 'id_user'

    
    category = forms.ChoiceField(choices=[], label='Categória')
    keyword = forms.CharField(label='Palavra-chave')
    user = forms.ChoiceField(choices=[], label='Usuários')
    function = forms.CharField(label='Função')

    
    class Meta:
        model = Project
        fields = ['logo', 'title', 'description', 'content']

        labels = {
            'logo': 'Logo',
            'title': 'Título',
            'description': 'Descrição',
            'content': 'Conteúdo',
        }
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'project-logo', 'hidden': 'true'}),
            'title': forms.TextInput(attrs={'class': 'project-title'}),
            'description': forms.Textarea(attrs={'class': 'project-description', 'rows': 5}),
        }


    def get_category_choices(self):
        categories = Category.objects.all()
        choices = [(category.id, category.name) for category in categories]
        return choices
    
    def get_user_choices(self):
        users = User.objects.all()
        choices = [(user.username, user.username) for user in users]
        return choices