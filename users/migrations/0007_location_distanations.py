# Generated by Django 3.2.9 on 2023-06-15 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='distanations',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
