# Generated by Django 5.1.3 on 2024-11-25 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0037_delete_passwordreset'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaystackPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]