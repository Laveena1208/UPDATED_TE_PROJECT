# Generated by Django 3.2.7 on 2022-02-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_remove_result_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result12comm',
            name='answer',
            field=models.CharField(choices=[('Dislike', 'Dislike'), ('Neutral', 'Neutral'), ('Enjoy', 'Enjoy')], max_length=1000),
        ),
    ]
