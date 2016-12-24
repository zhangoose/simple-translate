# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('original_text', models.TextField()),
                ('translated_text', models.TextField()),
                ('language', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, null=True, blank=True)),
            ],
        ),
    ]
