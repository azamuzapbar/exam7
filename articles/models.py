from django.db import models

# Create your models here.
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    ACTIVE='ACTIVE', 'Активна',
    NOT_ACTIVE= 'NOT_ACTIVE', 'Не активна'

class Guest(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200, null=False, blank=False)
    text = models.TextField(verbose_name='Текст', max_length=2000, null=False, blank=False)
    email=models.EmailField(verbose_name='мэйл',max_length=200,)
    author = models.TextField(verbose_name='Автор', max_length=3000, null=False, blank=False, default='')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    status=models.CharField(verbose_name='Статус', choices=StatusChoices.choices, max_length=100, default=StatusChoices.ACTIVE)

    def __str__(self):
        return f'{self.title} {self.author} {self.email}'
