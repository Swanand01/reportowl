# Generated by Django 3.2.8 on 2021-11-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0007_auto_20211101_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='slug',
            field=models.SlugField(max_length=110),
        ),
    ]
