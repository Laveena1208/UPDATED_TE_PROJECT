# Generated by Django 3.2.8 on 2022-01-18 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20220118_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='username',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
