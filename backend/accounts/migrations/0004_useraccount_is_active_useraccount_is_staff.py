# Generated by Django 4.2.2 on 2023-06-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_useraccount_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
