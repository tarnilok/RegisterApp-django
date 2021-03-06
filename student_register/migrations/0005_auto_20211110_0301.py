# Generated by Django 3.2.8 on 2021-11-10 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0004_alter_studentinfo_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='path',
            field=models.CharField(choices=[('fullstack', 'FullStack'), ('datascience', 'DataScience'), ('awsdevops', 'Aws&Devops')], max_length=20),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='photo',
            field=models.URLField(),
        ),
    ]
