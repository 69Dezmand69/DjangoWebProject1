# Generated by Django 2.2.28 on 2024-12-15 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20241215_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 15, 15, 37, 14, 700113), verbose_name='Дата комментария'),
        ),
    ]
