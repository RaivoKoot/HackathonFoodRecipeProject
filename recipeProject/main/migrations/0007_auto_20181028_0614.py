# Generated by Django 2.1.2 on 2018-10-28 06:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181028_0612'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Container',
            new_name='Inventory',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 28, 6, 14, 21, 250817, tzinfo=utc)),
        ),
    ]
