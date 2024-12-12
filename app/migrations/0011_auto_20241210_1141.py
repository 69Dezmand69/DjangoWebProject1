# Generated by Django 2.2.28 on 2024-12-10 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20241205_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 10, 11, 41, 22, 633631), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='videogame',
            name='genres',
            field=models.CharField(choices=[('Экшн', 'Экшн'), ('Приключение', 'Приключение'), ('Стратегия', 'Стратегия'), ('Хорор', 'Хорор'), ('Песочница', 'Песочница'), ('Аркада', 'Аркада')], max_length=100, verbose_name='Жанры'),
        ),
    ]
