# Generated by Django 3.1.7 on 2021-03-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_treasure_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
