# Generated by Django 2.0.5 on 2020-04-22 01:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='Address',
            field=models.CharField( max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='Contact',
            field=models.CharField( max_length=30),
            preserve_default=False,
        ),
    ]
