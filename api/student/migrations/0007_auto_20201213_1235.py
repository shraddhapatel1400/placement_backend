# Generated by Django 3.0.11 on 2020-12-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_student_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
