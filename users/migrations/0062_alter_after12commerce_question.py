# Generated by Django 3.2.7 on 2022-07-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0061_auto_20220425_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='after12commerce',
            name='question',
            field=models.CharField(max_length=900, unique=True),
        ),
    ]
