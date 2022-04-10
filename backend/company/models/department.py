from django.db import models


class Department(models.Model):
    name = models.CharField('Название', max_length=255)

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'

    def __str__(self):
        return f'{self.name}'
