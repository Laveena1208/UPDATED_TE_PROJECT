# Generated by Django 3.2.7 on 2022-02-25 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0054_auto_20220225_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result12arts',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='result12arts',
            name='question',
        ),
        migrations.RemoveField(
            model_name='result12arts',
            name='question_type',
        ),
        migrations.RemoveField(
            model_name='result12arts',
            name='username',
        ),
    ]
