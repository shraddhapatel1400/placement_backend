# Generated by Django 3.0.11 on 2020-12-21 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizScore', '0004_quizscore_correct_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizscore',
            name='correct_answer',
        ),
    ]
