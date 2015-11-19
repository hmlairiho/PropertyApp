# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20151118_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
