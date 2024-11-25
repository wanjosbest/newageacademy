# Generated by Django 4.2 on 2024-11-21 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0028_coursetimetable_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='coursemodule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=30, null=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='availablecoursemodules', to='Users.available_courses')),
            ],
        ),
    ]
