# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0006_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='referer_link',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]
