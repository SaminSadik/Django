# Generated by Django 5.0 on 2024-04-26 07:07

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(default='', max_length=20)),
                ('roll', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('father_name', models.CharField(default='', max_length=20)),
                ('address', models.TextField(default='')),
                ('date_field', models.DateField(default=datetime.datetime.today)),
                ('duration_field', models.DurationField(default=datetime.timedelta(0))),
                ('email_field', models.EmailField(default='example@gmail.com', max_length=254)),
                ('null_boolean_field', models.BooleanField(blank=True, default=None, null=True)),
                ('time_field', models.TimeField(default=django.utils.timezone.now)),
                ('url_field', models.URLField(default='http://google.com')),
            ],
        ),
    ]