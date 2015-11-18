# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=50)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('available', models.IntegerField(default=1)),
            ],
        ),
    ]
