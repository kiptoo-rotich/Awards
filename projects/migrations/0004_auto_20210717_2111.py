# Generated by Django 3.2.5 on 2021-07-17 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210717_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='technologies',
        ),
    ]
