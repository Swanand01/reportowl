# Generated by Django 3.2.8 on 2021-10-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0004_auto_20211030_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='slug',
            field=models.SlugField(max_length=110),
        ),
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(max_length=110),
        ),
    ]
