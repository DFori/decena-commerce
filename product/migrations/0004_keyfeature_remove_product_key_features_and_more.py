# Generated by Django 5.0.3 on 2024-03-28 13:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_category_options_product_key_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='key_features',
        ),
        migrations.CreateModel(
            name='ProductKeyFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.keyfeature')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
