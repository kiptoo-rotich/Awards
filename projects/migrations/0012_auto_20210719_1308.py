# Generated by Django 3.2.5 on 2021-07-19 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20210719_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projects'),
        ),
    ]
