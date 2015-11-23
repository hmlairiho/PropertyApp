# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0009_news_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_link',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
