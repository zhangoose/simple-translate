# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0002_auto_20161226_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='language',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
