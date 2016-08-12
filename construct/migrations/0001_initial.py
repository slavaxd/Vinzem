# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('datetime', models.DateTimeField()),
                ('service', models.TextField()),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img')),
                ('text', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField()),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0456\u044f',
                'verbose_name_plural': '\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0456\u0457',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img')),
                ('title', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField()),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0432\u0438\u043d\u0430',
                'verbose_name_plural': '\u041d\u043e\u0432\u0438\u043d\u0438',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/img')),
                ('title', models.TextField(max_length=300)),
                ('content', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440\u0438',
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('title', models.TextField(max_length=300)),
                ('content', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0447\u043d\u0430 \u0441\u0442\u043e\u0440\u0456\u043d\u043a\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0447\u043d\u0456 \u0441\u0442\u043e\u0440\u0456\u043d\u043a\u0438',
            },
        ),
    ]
