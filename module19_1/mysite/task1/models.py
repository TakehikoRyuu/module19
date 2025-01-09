from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100) #имя покупателя(username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2,default=0) #баланс(DecimalField)
    age = models.IntegerField(default=1, null=False) #возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100) #название игры
    cost = models.DecimalField(default=59.99, max_digits=10, decimal_places=2) #цена
    size = models.DecimalField(null=True, max_digits=5, decimal_places=1) #размер файлов игры
    description = models.CharField(max_length=1000) #описание
    age_limited = models.BooleanField(default=False) #ограничение возраста 18+
    buyer = models.ManyToManyField(Buyer, related_name='game') #1 Game ко многим Buyer

    def __str__(self):
        return self.title

# Create your models here.
