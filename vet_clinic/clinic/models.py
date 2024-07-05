from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Veterinerian(models.Model):
    '''Модель ветиринара'''
    name = models.CharField(
        max_length=50,
        verbose_name='Имя',
        null=False,
        blank=False,
    )
    surname = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
        null=False,
        blank=False,
    )
    patronymic = models.CharField(
        max_length=50,
        verbose_name='Отчество',
        null=False,
        blank=True,
    )
    photo = models.ImageField(
        upload_to='vet/images/',
        verbose_name='Фото',
        null=False,
        blank=True,
    )
    professions = models.ManyToManyField(
        'Profession',
        verbose_name='Профессия',
        related_name='veterinerians',
        null=False,
        blank=False,
    )
    specializations = models.ManyToManyField(
        'Specialization',
        on_delete=models.CASCADE,
        verbose_name='Специализация',
        related_name='veterinerians',
        null=False,
        blank=False,
    )
    achievements = models.ManyToManyField(
        'Achievements',
        on_delete=models.CASCADE,
        verbose_name='Достижения',
        related_name='veterinerians',
        null=False,
        blank=False,
    )

    education = models.ManyToManyField(
        'Education',
        on_delete=models.CASCADE,
        verbose_name='Образование',
        related_name='veterinerians',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Ветеринар'
        verbose_name_plural = 'Ветеринары'

    def __str__(self):
        return self.name + self.surname


class Profession(models.Model):
    '''Модель профессии'''
    title = models.CharField(
        max_length=80,
        unique=True,
        verbose_name='Название',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title


class Specialization(models.Model):
    '''Модель специализации'''
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Achievements(models.Model):
    '''Модель достижения'''
    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='Название',
    )

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def __str__(self):
        return self.name


class Clinic(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название',
        null=False,
        blank=False,
    )
    poster = models.ImageField(
        upload_to='clinic/images/',
        verbose_name='Постер',
    )
    icon = models.ImageField(
        upload_to='clinic/images/',
        verbose_name='Иконка',
    )
    about_clinic = models.TextField(
        blank=True,
        verbose_name='О клинике',
        null=False,
    )
    address = models.CharField(
        max_length=100,
        verbose_name='Адрес',
        null=False,
        blank=True,
    )
    work_time_start = models.TimeField(
        verbose_name='Время работы',
        null=False,
        blank=True,
    )
    work_time_end = models.TimeField(
        verbose_name='Время работы',
        null=False,
        blank=True,
    )
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=True,
        verbose_name='Телефон',
    )
    veterinerians = models.ManyToManyField(
        Veterinerian,
        verbose_name='Ветеринары',
        related_name='clinics',
        null=False,
        blank=False,
    )

    priority = models.PositiveIntegerField(
        default=0,
        null=False,
        blank=False,
        verbose_name='Приоритетность',
    )

    class Meta:
        verbose_name = 'Клиника'
        verbose_name_plural = 'Клиники'
        ordering = ['priority']

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название',
        null=False,
        blank=False,
    )
    price = models.FloatField(
        blank=True,
        verbose_name='Цена',
    )

    clinic = models.ForeignKey(
        Clinic,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='Клиника',
        blank=False,
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title
