"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from django.urls import reverse



class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовок")

    description = models.TextField(verbose_name="Краткое содержание")

    content = models.TextField(verbose_name="Полное содержание")

    posted = models.DateTimeField(default = datetime.now, db_index=True, verbose_name="Опубликована")

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Автор")

    image = models.FileField(default = 'temp.jpg', verbose_name="Путь к картинке")


    # методы класса
    def get_absolute_url(self):  # метод возвращает строку с URL-адресом записи
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):  # метод возвращает название, используемое для представления отдельных записей в адм. разделе
        return self.title

    # метаданные - вложенный в класс, который задает дополнительные параметры модели:
    class Meta:
        db_table = "Posts"  # имя таблицы для модели
        ordering = ["-posted"]  # порядок сортировки данных в модели ("-" означает убывание)
        verbose_name = "статья блога"  # имя, под которым модель будет отображаться в адм. разделе (для одной статьи блога)
        verbose_name_plural = "статьи блога"  # тоже для всех статей блога

# Регистрация модели в админке
admin.site.register(Blog)

# Create your models here.
class Comment(models.Model):

    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Дата комментария")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор комментария")
    post = models.ForeignKey('Blog', on_delete=models.CASCADE, verbose_name="Статья комментария")

    def __str__(self):

        return 'Комментарий %d %s к %s' % (self.id, self.author, self.post)

    class Meta:

        db_table = "Comment"

        ordering = ["-date"]

        verbose_name = "Комментарий к статье блога"

        verbose_name_plural = "Комментарии к статьям блога"

admin.site.register(Comment)

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, null=True, blank=True)  # Используем CharField для хранения пути к изображению

    def __str__(self):
        return self.title


class Genre(models.Model):
    GENRE_CHOICES = [
        ('Экшн', 'Экшн'),
        ('Приключение', 'Приключение'),
        ('Стратегия', 'Стратегия'),
        ('Хорор', 'Хорор'),
        ('Песочница', 'Песочница'),
        ('Аркада', 'Аркада'),
    ]
    name = models.CharField(max_length=50, choices=GENRE_CHOICES, unique=True)

    def __str__(self):
        return self.name
admin.site.register(Genre)



class VideoGame(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название игры")
    description = models.TextField(default='', verbose_name="Описание")
    image = models.FileField(default='temp.jpg', verbose_name="Путь к картинке")
    genres = models.ManyToManyField('Genre', verbose_name="Жанры")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def get_absolute_url(self):
        return reverse("videogame", args=[str(self.id)])

    def __str__(self):
        return self.title

    class Meta:
        db_table = "VideoGames"
        verbose_name = "видеоигра"
        verbose_name_plural = "видеоигры"
admin.site.register(VideoGame)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.game.title}"

    def total_price(self):
        return self.quantity * self.game.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderQuerySet(models.QuerySet):
    def by_client(self, client):
        return self.filter(client=client)

    def by_status(self, status):
        return self.filter(status=status)

    def recent_orders(self):
        return self.order_by('-order_date')

class VideoGameComment(models.Model):
    game = models.ForeignKey(VideoGame, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Содержание")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"

    class Meta:
        db_table = "VideoGameComments"
        verbose_name = "комментарий к видеоигре"
        verbose_name_plural = "комментарии к видеоиграм"



class Feedback(models.Model):
    nickname = models.CharField(max_length=100)
    game = models.ForeignKey(VideoGame, on_delete=models.CASCADE)
    speed = models.IntegerField()
    price = models.IntegerField()
    service = models.IntegerField()
    message = models.TextField()
    average_rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.nickname} on {self.game}"