# Generated by Django 4.2.1 on 2023-05-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0006_remove_keyword_project_project_keyword'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(blank=True, default='', upload_to='proj/img/%Y/%m/%d/'),
        ),
    ]
