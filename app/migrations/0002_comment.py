# Generated by Django 2.2.28 on 2024-11-18 17:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('date', models.DateTimeField(db_index=True, default=datetime.datetime(2024, 11, 18, 20, 6, 36, 669061), verbose_name='Дата комментария')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Blog', verbose_name='Статья комментария')),
            ],
            options={
                'verbose_name': 'Комментарий к статье блога',
                'verbose_name_plural': 'Комментарии к статьям блога',
                'db_table': 'Comment',
                'ordering': ['-date'],
            },
        ),
    ]
