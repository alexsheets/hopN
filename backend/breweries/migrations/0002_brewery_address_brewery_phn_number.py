# Generated by Django 4.1.2 on 2022-10-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='brewery',
            name='phn_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]