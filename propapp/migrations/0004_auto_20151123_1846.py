# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0003_general_options_prop_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='property_id',
        ),
        migrations.AddField(
            model_name='property',
            name='id',
            field=models.AutoField(default=0, serialize=False, auto_created=True, primary_key=True, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
