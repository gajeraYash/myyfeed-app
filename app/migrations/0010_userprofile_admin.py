# Generated by Django 3.1.2 on 2020-10-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20201008_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
