# Generated by Django 4.2 on 2024-12-01 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0064_user_referal_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referrer',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
