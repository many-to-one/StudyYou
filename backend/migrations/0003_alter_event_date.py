# Generated by Django 4.1.5 on 2023-02-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_event_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
