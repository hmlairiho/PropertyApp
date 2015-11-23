# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propapp', '0005_auto_20151123_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('referer_link', models.CharField(max_length=30)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
