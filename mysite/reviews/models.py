from django.db import models

# Create your models here.
class Articles(models.Model):
    name = models.CharField('Имя', max_length=50)
    anons = models.CharField('Тема', max_length=250)
    full_text = models.TextField('Отзыв')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'