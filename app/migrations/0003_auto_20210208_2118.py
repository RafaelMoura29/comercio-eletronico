# Generated by Django 2.2.3 on 2021-02-09 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product_fk',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_fk',
            field=models.ManyToManyField(blank=True, to='app.Product'),
        ),
    ]
