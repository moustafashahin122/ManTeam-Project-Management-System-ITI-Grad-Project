# Generated by Django 4.2.2 on 2023-06-21 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_clone_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='clone_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]