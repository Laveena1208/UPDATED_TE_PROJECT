# Generated by Django 3.2.7 on 2022-02-07 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_auto_20220207_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='After10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=900, unique=True)),
                ('question_type', models.CharField(default=' ', max_length=120)),
                ('op1', models.CharField(max_length=900, null=True)),
                ('op2', models.CharField(max_length=900, null=True)),
                ('op3', models.CharField(max_length=900, null=True)),
                ('op4', models.CharField(max_length=900, null=True)),
                ('correct_answer', models.CharField(default=' ', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(blank=True, max_length=254)),
                ('question', models.CharField(default='', max_length=1000)),
                ('answer', models.CharField(choices=[('op1', 'Dislike'), ('op2', 'Neutral'), ('op3', 'Enjoy')], max_length=900)),
                ('question_type', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Result10Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('count_science', models.CharField(max_length=10)),
                ('count_arts', models.CharField(max_length=10)),
                ('count_commerce', models.CharField(max_length=10)),
                ('count_diploma', models.CharField(default=' ', max_length=10)),
            ],
        ),
    ]
