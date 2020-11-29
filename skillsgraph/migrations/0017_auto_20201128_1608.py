# Generated by Django 3.1.3 on 2020-11-28 16:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skillsgraph', '0016_auto_20201128_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 8, 32, 158568, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_job',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 8, 32, 159658, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_skill',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 16, 8, 32, 160031, tzinfo=utc)),
        ),
    ]