# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20150109_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialty',
            name='specialty_type',
            field=models.CharField(max_length=2, null=True, choices=[(b'EN', '\u5de5\u79d1'), (b'SC', '\u7406\u79d1'), (b'BU', '\u5546\u79d1'), (b'AR', '\u827a\u672f')]),
            preserve_default=True,
        ),
    ]
