# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0008_auto_20160812_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img')),
                ('name', models.TextField(max_length=300)),
                ('description', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': '\u041b\u044e\u0434\u0438\u043d\u0430',
                'verbose_name_plural': '\u041b\u044e\u0434\u0438',
            },
        ),
    ]
