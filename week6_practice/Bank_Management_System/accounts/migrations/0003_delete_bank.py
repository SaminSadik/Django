# Generated by Django 5.0 on 2024-09-21 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_bank'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bank',
        ),
    ]
