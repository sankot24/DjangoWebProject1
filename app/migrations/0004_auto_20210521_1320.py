# Generated by Django 2.2.20 on 2021-05-21 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210521_1221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-posted'], 'verbose_name': 'статья блога', 'verbose_name_plural': 'статьи блога'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 5, 21, 13, 20, 57, 791152), verbose_name='Опубликована'),
        ),
    ]
