# Generated by Django 5.0 on 2024-05-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_mainmodel_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainmodel',
            name='img',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
