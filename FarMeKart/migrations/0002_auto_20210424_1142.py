# Generated by Django 3.0 on 2021-04-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FarMeKart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vegpro',
            name='is_farmer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vegpro',
            name='is_stock',
            field=models.IntegerField(default=0),
        ),
    ]