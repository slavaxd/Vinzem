# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0021_auto_20161121_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkHours',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', ckeditor.fields.RichTextField(max_length=100000)),
            ],
            options={
                'verbose_name': '(\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0438) \u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u0433\u043e\u0434\u0438\u043d \u0440\u043e\u0431\u043e\u0442\u0438 \u0442\u0430 \u043c\u0456\u0441\u0446\u0435\u0437\u043d\u0430\u0445\u043e\u0434\u0436\u0435\u043d\u043d\u044f',
                'verbose_name_plural': '(\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u0438) \u041f\u043e\u043b\u0435 \u0434\u043b\u044f \u0433\u043e\u0434\u0438\u043d \u0440\u043e\u0431\u043e\u0442\u0438 \u0442\u0430 \u043c\u0456\u0441\u0446\u0435\u0437\u043d\u0430\u0445\u043e\u0434\u0436\u0435\u043d\u043d\u044f',
            },
        ),
        migrations.AlterModelOptions(
            name='indexbehindlink',
            options={'verbose_name': '\u041f\u043e\u043b\u0435 \u0432\u043d\u0438\u0437\u0443 \u0437 HTML', 'verbose_name_plural': '\u041f\u043e\u043b\u0435 \u0432\u043d\u0438\u0437\u0443 \u0437 HTML'},
        ),
    ]
