# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0010_auto_20151123_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='general_options',
            name='front_title',
            field=models.CharField(max_length=30),
        ),
    ]
