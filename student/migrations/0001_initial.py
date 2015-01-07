# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_local', models.CharField(default=b'', max_length=200)),
                ('name_cn', models.CharField(max_length=200)),
                ('adress', models.CharField(default=b'', max_length=200)),
                ('country', models.CharField(default=b'', max_length=30)),
                ('city', models.CharField(default=b'', max_length=50)),
                ('code_postal', models.CharField(default=b'', max_length=10)),
                ('site', models.CharField(default=b'', max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('detail', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Situation_school',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_end', models.DateField(null=True)),
                ('date_start', models.DateField()),
                ('is_end', models.BooleanField(default=True)),
                ('is_pub', models.BooleanField(default=True)),
                ('school', models.ForeignKey(to='student.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_local', models.CharField(default=b'', max_length=200)),
                ('name_cn', models.CharField(max_length=200)),
                ('detail', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_cn', models.CharField(default=b'', max_length=30)),
                ('telephone_protable', models.CharField(max_length=16)),
                ('adress', models.CharField(default=b'', max_length=200)),
                ('country', models.CharField(default=b'China', max_length=30)),
                ('city', models.CharField(default=b'', max_length=50)),
                ('code_postal', models.CharField(default=b'', max_length=10)),
                ('gender', models.BooleanField(default=True, choices=[(True, b'man'), (False, b'woman')])),
                ('date_naissance', models.DateField(null=True)),
                ('year_in_school', models.CharField(default=b'FR', max_length=3, choices=[(b'FR', b'Freshman'), (b'SO', b'Sophomore'), (b'JR', b'Junior'), (b'SR', b'Senior'), (b'M', b'Master'), (b'PHD', b'Doctor')])),
                ('qq_link', models.CharField(default=b'', max_length=30)),
                ('site', models.URLField(default=b'')),
                ('facebook_link', models.URLField(default=b'')),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='student.Student')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='situation_school',
            name='specialty',
            field=models.ForeignKey(to='student.Specialty'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='situation_school',
            name='student',
            field=models.ForeignKey(to='student.Student'),
            preserve_default=True,
        ),
    ]
