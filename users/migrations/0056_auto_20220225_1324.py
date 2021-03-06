# Generated by Django 3.2.7 on 2022-02-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0055_auto_20220225_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='result12arts',
            name='answer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='result12arts',
            name='question',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='result12arts',
            name='question_type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='result12arts',
            name='username',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
