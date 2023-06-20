# Generated by Django 4.2.2 on 2023-06-20 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('t', 'TO Do'), ('p', 'In Progress'), ('t', 'Testing'), ('f', 'Failed'), ('d', 'Done'), ('c', 'Canceled')], default='t', max_length=1),
        ),
    ]
