# Generated by Django 3.2.8 on 2021-10-21 11:23

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male'), ('other', 'Other')], max_length=10)),
                ('student_number', models.CharField(max_length=50, unique=True)),
                ('path', models.CharField(choices=[('awsdevops', 'Aws&Devops'), ('fullstack', 'FullStack'), ('datascience', 'DataScience')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Student_List',
                'db_table': 'StudentInfo',
                'ordering': ['student_number'],
            },
        ),
    ]
