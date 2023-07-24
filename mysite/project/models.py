from django.db import models
from django_summernote.fields import SummernoteTextField
from django.contrib.auth.models import User


class Category(models.Model):
   name = models.CharField(max_length=65, null=False, blank=False)

   def __str__(self):
      return f"{self.id} - {self.name}"


class Keyword(models.Model):
   name = models.CharField(max_length=50, null=False, blank=False)
   
   def __str__(self):
      return f"{self.id} - {self.name}"


STATUS_CHOICES = (
      ('em_andamento', 'Em Andamento'),
      ('finalizado', 'Finalizado'),
   )

class Project(models.Model):
   logo = models.ImageField(upload_to='proj/img/%Y/%m/%d/', blank=True, default='')
   title = models.CharField(max_length=65)
   description = models.CharField(max_length=150)
   date_create = models.DateField(auto_now_add=True)
   content = SummernoteTextField()
   status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em_andamento')
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
   keyword = models.ManyToManyField(Keyword)

   def __str__(self):
      return f"{self.id} - {self.title}"

class Function(models.Model):
   name = models.CharField(max_length=50, null=False, blank=False)
   def __str__(self):
      return f"{self.id} - {self.name}"

class Involvement(models.Model):
   date_start = models.DateTimeField(auto_now_add=True)
   date_finish = models.DateTimeField(default=None, blank=True, null=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, default=None)
   function = models.ForeignKey(Function, on_delete=models.SET_DEFAULT, default=None)
   def __str__(self):
      return f"{self.id} - {self.user.username}/{self.project.title}"


