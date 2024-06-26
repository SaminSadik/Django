# Generated by Django 5.0 on 2024-05-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4models', '0002_mymodel_remove_mytable_address_remove_mytable_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='email_address',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='mymodel',
            name='profile',
            field=models.URLField(null=True),
        ),
    ]
