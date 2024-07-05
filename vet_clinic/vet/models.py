from django.db import models

class Vet(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    image = models.ImageField(upload_to='vet/images/') 

    class Meta:
        verbose_name = 'Ветеринар'
        verbose_name_plural = 'Ветеринары'


    def __str__(self):
        return self.name + self.surname 


class Profession(models.Model):
    title = models.CharField(max_length=80)
    vet = models.ManyToManyField(Vet, verbose_name='Ветеринар', 
                                 related_name='professions')

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


    def __str__(self):
        return self.title 

class Specialization(models.Model):
    name = models.CharField(max_length=100)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, 
                            verbose_name='Специализация',
                            related_name='specialization')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name 

class Achievements(models.Model):
    name = models.CharField(max_length=100)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, 
                            verbose_name='Достижения',
                            related_name='achievements')

    class Meta:
        verbose_name = 'Достижения'
        verbose_name_plural = 'Достижения'


class Education(models.Model):
    name = models.CharField(max_length=100)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, 
                            verbose_name='Образование',
                            related_name='education')

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'


    def __str__(self):
        return self.name 