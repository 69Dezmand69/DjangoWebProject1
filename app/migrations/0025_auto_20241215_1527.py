# Generated by Django 2.2.28 on 2024-12-15 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20241215_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videogamecomment',
            options={'verbose_name': 'комментарий к видеоигре', 'verbose_name_plural': 'комментарии к видеоиграм'},
        ),
        migrations.AddField(
            model_name='videogamecomment',
            name='rating',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, verbose_name='Рейтинг'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 12, 15, 15, 24, 40, 63864), verbose_name='Дата комментария'),
        ),
        migrations.AlterField(
            model_name='videogamecomment',
            name='content',
            field=models.TextField(verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='videogamecomment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterModelTable(
            name='videogamecomment',
            table='VideoGameComments',
        ),
        migrations.DeleteModel(
            name='VideoGameRating',
        ),
    ]
