# Generated by Django 5.1.3 on 2024-11-14 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0016_rename_course_studentattendance_course_code_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='studentattendance',
        ),
    ]
