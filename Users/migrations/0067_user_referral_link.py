# Generated by Django 4.2 on 2024-12-01 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0066_remove_user_referal_link_remove_user_referral_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='referral_link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
