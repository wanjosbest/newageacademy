# Generated by Django 4.2 on 2024-11-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0024_createassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
