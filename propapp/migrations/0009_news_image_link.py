# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0008_auto_20151123_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_link',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
