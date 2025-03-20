from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='Порода')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'
        ordering = ['name',]


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    # category = models.CharField(max_length=100, verbose_name='Порода')
    breed = models.ForeignKey("dogs.Breed", on_delete=models.SET_NULL, **NULLABLE, verbose_name='Порода', related_name='dogs')
    photo = models.ImageField(upload_to='dog_photo', **NULLABLE, verbose_name='Фото')
    date_born = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name} ({self.breed})'


    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ['breed', 'name',]


class Parent(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, verbose_name= "кличка собаки")
    name = models.CharField(max_length=250, verbose_name='Кличка')
    category = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода')
    birth_day = models.DateField(**NULLABLE, verbose_name='Дата рождения')

    def __str__(self):
        return f'{self.name} ({self.category})'


    class Meta:
        verbose_name = 'предок'
        verbose_name_plural = 'предки'





