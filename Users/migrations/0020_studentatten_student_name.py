# Generated by Django 5.1.3 on 2024-11-18 03:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0019_remove_studentatten_course_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentatten',
            name='student_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userattendance', to=settings.AUTH_USER_MODEL),
        ),
    ]
