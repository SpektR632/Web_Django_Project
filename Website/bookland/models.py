from django.db import models
from django.urls import reverse


# Create your models here.


class Book(models.Model):
    """
    Создание модели Book (книги) в модуле
    """
    title = models.CharField(max_length=200,
                             verbose_name='Название книги')
    genre = models.CharField(max_length=200,
                             verbose_name='Жанр книги',
                             blank=True)
    publisher = models.CharField(max_length=200,
                                 verbose_name='Издательство')
    year = models.CharField(max_length=4,
                            verbose_name='Год издательства')
    author = models.CharField(max_length=100,
                              verbose_name='Автор книги',
                              default='Нет автора')
    description = models.TextField(max_length=2000,
                                   verbose_name='Аннотация книги')
    isbn = models.CharField(max_length=20,
                            verbose_name='ISBN  книги')
    price = models.CharField(max_length=10,
                             verbose_name='Цена (руб.)')
    photo = models.ImageField(upload_to='Website/parcer/images/',
                              verbose_name='Изображение обложки')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Функция позволяет сопоставить URL-адреса с соответствующим шаблоном HTML-страницы
        :return: Возвращает URL-адрес для доступа к определенному экземпляру книги
        """
        return reverse('book-detail', args=(str(self.id)))

