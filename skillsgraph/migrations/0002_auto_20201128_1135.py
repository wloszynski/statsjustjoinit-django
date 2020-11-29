# Generated by Django 3.1.3 on 2020-11-28 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('skillsgraph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='last_update',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 11, 35, 38, 171535, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_jobs',
            name='data_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 11, 35, 38, 172587, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='overtime_skills',
            name='data_created',
            field=models.DateField(default=datetime.datetime(2020, 11, 28, 11, 35, 38, 172995, tzinfo=utc)),
        ),
    ]