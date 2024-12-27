# Generated by Django 5.0.3 on 2024-12-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_rename_user_email_order_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delayed', 'Delayed'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=10),
        ),
    ]
