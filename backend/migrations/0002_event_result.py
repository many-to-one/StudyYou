# Generated by Django 4.1.5 on 2023-01-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='result',
            field=models.IntegerField(default=0),
        ),
    ]
