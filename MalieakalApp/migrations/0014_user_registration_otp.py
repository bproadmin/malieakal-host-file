# Generated by Django 3.2.20 on 2023-08-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0013_auto_20230808_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='otp',
            field=models.IntegerField(default=0),
        ),
    ]
