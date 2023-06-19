# Generated by Django 3.2.9 on 2023-06-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_mini',
        ),
        migrations.RemoveField(
            model_name='product',
            name='number_of_product',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]