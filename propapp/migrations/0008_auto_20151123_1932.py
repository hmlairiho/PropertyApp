# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0007_auto_20151123_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='referer_link',
            field=models.CharField(max_length=150),
        ),
    ]
