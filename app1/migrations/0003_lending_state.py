# Generated by Django 3.2.17 on 2023-03-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_lending'),
    ]

    operations = [
        migrations.AddField(
            model_name='lending',
            name='State',
            field=models.IntegerField(default=0),
        ),
    ]
