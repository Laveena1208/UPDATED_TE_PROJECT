# Generated by Django 3.2.7 on 2022-02-07 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0050_alter_after10_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='after10',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
