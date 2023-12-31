# Generated by Django 4.2.3 on 2023-07-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='involvement',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('em_andamento', 'Em Andamento'), ('finalizado', 'Finalizado')], default='em_andamento', max_length=20),
        ),
    ]
