# Generated by Django 3.2.7 on 2021-09-23 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_listings_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='picture',
            new_name='image',
        ),
    ]
