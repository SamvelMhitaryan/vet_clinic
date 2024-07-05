from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female')]
    image = models.ImageField(upload_to='user/images/')
    patronymic = models.CharField(max_length=100)
    bithday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    notificate_sms = models.BooleanField(blank=False, null=True)
    notificate_email = models.BooleanField(blank=False, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        

    def __str__(self):
        return self.first_name    