from django.db import models

class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='Название новости')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Текст новости')
    date = models.DateTimeField('Время новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'