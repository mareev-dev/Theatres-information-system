
from django.db import models
from django.forms import CharField


# Create your models here.


    

class Salon(models.Model):
    """
    name
    address
    phone
    email
    descrtiption
    owner
    time_in
    time_out
    image
    """
    # social = models.ForeignKey(Social, on_delete=models.CASCADE, verbose_name='Соц сеть')
    name = models.CharField(verbose_name = 'Название салона', max_length = 256)
    address = models.CharField(verbose_name='Адрес', max_length=256)
    phone = models.CharField(verbose_name='Телефон', max_length=256)
    email = models.CharField(verbose_name='email', max_length=256)
    description = models.TextField(verbose_name='Описание')
    # owner = models.OneToOne
    time_in = models.TimeField(verbose_name='Время начала работы')
    time_out = models.TimeField(verbose_name='Время окончания работы')
    image = models.ImageField(verbose_name='Картинка салона', upload_to='images/salons/')
    

    def __str__(self):
        return self.name

class Social(models.Model):
    """
    name -models.CharField
    url - models.CharField

    """
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name='Салон')
    name = models.CharField(verbose_name='Название соц. сети', max_length=256)
    url = models.CharField(verbose_name='URL', max_length=256)

    def __str__(self):
        return self.name

class Master(models.Model):
    """
    salon
    name
    last_name
    rank
    image 
    """
    RANK = (
        ('JR', 'Младший'),
        ('MD', 'Мастер'),
        ('TP', 'Топ'),
    )
    salon = models.OneToOneField(Salon, on_delete=models.CASCADE, verbose_name='Салон')
    fits_name = models.CharField(verbose_name='Имя мастера', max_length=256)
    last_name = models.CharField(verbose_name='Фамилия мастера', max_length=256)
    rank = models.CharField(verbose_name='Ранг мастера', max_length=256, choices=RANK)
    image = models.ImageField(verbose_name='Картинка мастера', upload_to='salons/')