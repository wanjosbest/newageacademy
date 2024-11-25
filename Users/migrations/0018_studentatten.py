# Generated by Django 5.1.3 on 2024-11-14 23:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0017_delete_studentattendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentatten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_email', models.EmailField(max_length=100, null=True, unique=True, verbose_name='Student Email')),
                ('course_name', models.CharField(max_length=50, null=True, verbose_name='Attendance Course Name')),
                ('status', models.CharField(choices=[('P', 'PRESENT'), ('A', 'ABSENT')], default='PRESENT', max_length=10)),
                ('entry_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('course_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courseattendance', to='Users.available_courses')),
            ],
            options={
                'verbose_name': 'studentattendance',
                'verbose_name_plural': 'Student Attendance',
            },
        ),
    ]
