# Generated by Django 3.2.8 on 2021-10-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='photo',
            field=models.ImageField(default='avatar.png', upload_to='profile_photos'),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='path',
            field=models.CharField(choices=[('awsdevops', 'Aws&Devops'), ('datascience', 'DataScience'), ('fullstack', 'FullStack')], max_length=20),
        ),
    ]
