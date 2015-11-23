# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0004_auto_20151123_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='id',
        ),
        migrations.AddField(
            model_name='property',
            name='property_id',
            field=models.AutoField(default=0, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
