from django.db import models
from model_utils.models import TimeStampedModel


class Employee(TimeStampedModel):
    name = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['name']

    def __str__(self):
        return self.name
