# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20150107_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='country',
            field=models.CharField(max_length=2, null=True, choices=[(b'FR', b'France'), (b'EN', b'United kingdom'), (b'AU', b'Australia'), (b'CA', b'Canada'), (b'CH', b'Switzerland'), (b'DE', b'Germany'), (b'ES', b'Spain'), (b'KR', b'Korea'), (b'SG', b'Singapore'), (b'JP', b'Japan'), (b'IT', b'Italy'), (b'US', b'United States')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.CharField(max_length=2, null=True, choices=[(b'FR', b'France'), (b'EN', b'United kingdom'), (b'AU', b'Australia'), (b'CA', b'Canada'), (b'CH', b'Switzerland'), (b'DE', b'Germany'), (b'ES', b'Spain'), (b'KR', b'Korea'), (b'SG', b'Singapore'), (b'JP', b'Japan'), (b'IT', b'Italy'), (b'US', b'United States')]),
            preserve_default=True,
        ),
    ]
