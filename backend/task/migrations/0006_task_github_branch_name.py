# Generated by Django 4.2.2 on 2023-06-21 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='github_branch_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]