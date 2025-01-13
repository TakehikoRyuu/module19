from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100) #имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2,default=0) #баланс
    age = models.IntegerField(default=1, null=False) #возраст

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатель" #человеко-читаемое название для поля
        verbose_name_plural = "Покупатели" #человеко-читаемое название во множественном числе


class Game(models.Model):
    title = models.CharField(max_length=100) #название игры
    cost = models.DecimalField(default=59.99, max_digits=10, decimal_places=2) #цена
    size = models.DecimalField(null=True, max_digits=5, decimal_places=1) #размер файлов игры
    description = models.CharField(max_length=1000) #описание
    age_limited = models.BooleanField(default=False) #ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='game') #1 Game ко многим Buyer

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# применённые команды -
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell
# from task1.models import Buyer
# from task1.models import Game
# Hum1 = Buyer.objects.create(name='Max', balance=1500, age=25)
# Hum2 = Buyer.objects.create(name='Takehiko', balance=500, age=22)
# Hum3 = Buyer.objects.create(name='New', balance=50, age=16)
# game1 = Game.objects.create(title='GTA5', cost=15.99, size=112.1, description='Big game', age_limited=True)
# game2 = Game.objects.create(title='Warframe', cost=1.15, size=35.3, description='Long game', age_limited=True)
# game3 = Game.objects.create(title='Valheim', cost=9.99, size=8.5, description='Small game')
# Hum2.game.add(game1, game2)
# Hum1.game.add(game1, game2, game3)
# Hum3.game.add(game3)


# Create your models here.
