# Generated by Django 2.0.7 on 2018-08-09 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_auto_20180809_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venuedata',
            old_name='wheelchairaval',
            new_name='wheelchairavail',
        ),
    ]