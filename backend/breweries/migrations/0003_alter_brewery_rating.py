# Generated by Django 4.1.2 on 2022-10-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breweries', '0002_brewery_address_brewery_phn_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brewery',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
