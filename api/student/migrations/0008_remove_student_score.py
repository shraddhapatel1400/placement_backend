# Generated by Django 3.0.11 on 2020-12-22 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20201213_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='score',
        ),
    ]
