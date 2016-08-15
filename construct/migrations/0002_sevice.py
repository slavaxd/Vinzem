# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField()),
            ],
            options={
                'verbose_name': '\u041f\u043e\u0441\u043b\u0443\u0433\u0430',
                'verbose_name_plural': '\u041f\u043e\u0441\u043b\u0443\u0433\u0438',
            },
        ),
    ]
