# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Running', '0037_auto_20150708_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='end_date',
            field=models.DateField(default=datetime.date(2015, 7, 9), verbose_name=b'End Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='run',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 7, 9), verbose_name=b'Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='end_date',
            field=models.DateField(default=datetime.date(2015, 8, 9), null=True, verbose_name=b'End Date', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sponsorship',
            name='start_date',
            field=models.DateField(default=datetime.date(2015, 7, 9), null=True, verbose_name=b'Start Date', db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='wager',
            name='remind_date',
            field=models.DateField(default=datetime.date(2015, 8, 9), null=True, verbose_name=b'Remind Date'),
            preserve_default=True,
        ),
    ]
