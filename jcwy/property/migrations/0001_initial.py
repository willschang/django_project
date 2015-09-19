# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7ID')),
                ('user_name', models.CharField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xa7\x93\xe5\x90\x8d', max_length=20)),
                ('pwd', models.CharField(help_text=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\xaf\x86\xe7\xa0\x81', max_length=20)),
            ],
        ),
    ]
