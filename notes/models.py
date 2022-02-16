from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Note(models.Model):
    text = models.TextField(verbose_name='Текст')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заметку'
        verbose_name_plural = 'Заметки'

    def get_absolute_url(self):
        return reverse('home')
