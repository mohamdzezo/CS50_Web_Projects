# Generated by Django 3.2.7 on 2021-09-26 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_listings_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='owner',
        ),
    ]
