# Generated by Django 3.2.23 on 2023-11-09 11:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0016_alter_user_registration_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=255, null=True)),
                ('secondnumb', models.CharField(blank=True, max_length=255, null=True)),
                ('item', models.CharField(blank=True, max_length=255, null=True)),
                ('item_company', models.CharField(blank=True, max_length=255, null=True)),
                ('complaint', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('date_register', models.DateField(default=datetime.date(2023, 11, 9))),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='sub_category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='banner_access',
            field=models.CharField(blank=True, default='false', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='cat_access',
            field=models.CharField(blank=True, default='false', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='item_access',
            field=models.CharField(blank=True, default='false', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='offer_access',
            field=models.CharField(blank=True, default='false', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='order_access',
            field=models.CharField(blank=True, default='false', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile_user',
            name='user_access',
            field=models.CharField(blank=True, default='false', max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MalieakalApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='new_arrival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(default='static/images/logo/noimage.jpg', upload_to='images/items')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('price', models.FloatField(default=0)),
                ('offer_price', models.FloatField(default=0)),
                ('offer', models.IntegerField(default=0)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MalieakalApp.user_registration')),
            ],
        ),
    ]
