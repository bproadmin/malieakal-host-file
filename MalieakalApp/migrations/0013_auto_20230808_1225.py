# Generated by Django 3.2.20 on 2023-08-08 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MalieakalApp', '0012_auto_20230805_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='item',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='item_price',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='item_total',
        ),
        migrations.RemoveField(
            model_name='checkout',
            name='qty',
        ),
        migrations.AddField(
            model_name='checkout',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MalieakalApp.profile_user'),
        ),
        migrations.AddField(
            model_name='checkout',
            name='total_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.CreateModel(
            name='checkout_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(blank=True, max_length=255, null=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('item_price', models.FloatField(blank=True, null=True)),
                ('checkout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MalieakalApp.checkout')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MalieakalApp.item')),
            ],
        ),
    ]
