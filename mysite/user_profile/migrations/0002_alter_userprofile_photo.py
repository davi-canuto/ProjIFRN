# Generated by Django 4.2.1 on 2023-05-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='user_profile/img/%Y/%m/%d/'),
        ),
    ]
