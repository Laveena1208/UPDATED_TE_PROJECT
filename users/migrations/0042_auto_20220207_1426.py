# Generated by Django 3.2.7 on 2022-02-07 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20220207_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='answer',
            field=models.CharField(choices=[('op1', 'Dislike'), ('op2', 'Neutral'), ('op3', 'Enjoy')], max_length=900),
        ),
        migrations.AlterField(
            model_name='result',
            name='correct_answer',
            field=models.CharField(default=' ', max_length=900),
        ),
    ]
