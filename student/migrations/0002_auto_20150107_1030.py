# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='friends',
        ),
        migrations.AlterField(
            model_name='school',
            name='adress',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='city',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='code_postal',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='country',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='name_local',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='site',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='specialty',
            name='name_local',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='adress',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='code_postal',
            field=models.CharField(max_length=10, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='facebook_link',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='qq_link',
            field=models.CharField(max_length=30, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='site',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
