# Generated by Django 2.0.7 on 2018-08-17 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_auto_20180817_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venuedata',
            name='openperiods',
        ),
        migrations.AddField(
            model_name='openhours',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='restapi.VenueData', verbose_name='Venue'),
        ),
    ]
