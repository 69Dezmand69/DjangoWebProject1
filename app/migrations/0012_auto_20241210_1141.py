# Generated by Django 2.2.28 on 2024-12-10 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20241210_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 10, 11, 41, 30, 651039), verbose_name='Дата комментария'),
        ),
    ]