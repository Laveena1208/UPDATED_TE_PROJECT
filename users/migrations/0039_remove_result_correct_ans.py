# Generated by Django 3.2.7 on 2022-02-07 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_auto_20220207_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='correct_ans',
        ),
    ]
