# Generated by Django 4.2 on 2024-11-29 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0058_promotedcourses_description_promotedcourses_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='referal',
            name='referal_link',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]