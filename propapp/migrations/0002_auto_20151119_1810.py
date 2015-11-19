# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='code',
        ),
        migrations.RemoveField(
            model_name='property',
            name='id',
        ),
        migrations.AddField(
            model_name='property',
            name='property_id',
            field=models.AutoField(serialize=False, default=1, primary_key=True),
        ),
    ]
