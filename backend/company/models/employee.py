from django.db import models
from django.core.validators import MinValueValidator


class Employee(models.Model):
    PROGRAMMER = 'PR'
    MANAGER = 'MN'
    POSITION_CHOICES = (
        (PROGRAMMER, 'Программист'),
        (MANAGER, 'Менеджер'),
    )

    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255, db_index=True)
    middle_name = models.CharField('Отчество', max_length=255)
    position = models.CharField('Должность', choices=POSITION_CHOICES, max_length=2)
    salary = models.FloatField('Оклад', validators=[MinValueValidator(0.0)])
    age = models.PositiveSmallIntegerField('Возраст')
    department = models.ForeignKey(
        'company.Department',
        verbose_name='Департамент',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудник'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}, {self.age} лет'
