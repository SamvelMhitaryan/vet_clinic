from django.db import models
from user.models import User

class Kind(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'


    def __str__(self):
        return self.name 
    
class Breed(models.Model):
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE,
                             verbose_name='Порода',
                             related_name='breed')

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


    def __str__(self):
        return self.name 

class Health(models.Model):
    allergies = models.BooleanField(blank=False, null=True)
    castration = models.BooleanField(blank=False, null=True)

    class Meta:
        verbose_name = 'Здоровье'
        verbose_name_plural = 'Здоровье'

class Procedures(models.Model):
    veterinarian_check = models.DateField()
    vaccination = models.DateField()
    deworming = models.DateField()
    tick_flea_treatmen = models.DateField()

    class Meta:
        verbose_name = 'Процедуры'
        verbose_name_plural = 'Процедуры'

class Features(models.Model):
    FEATURES_CHOICES = [('Де','Дерматит'), ('По','Заболевание почек'), 
            ('Су','Заболевание суставов'), ('Ож','Ожирение'), 
            ('Мо','Мочекаменная болезнь'), ('Са','Сахарный диабет'),
            ('Се','Сердечная недостаточность'), 
            ('Чу','Чувствительное пищеварение'),('Бе','Беременность'), 
            ('Во','Восстановление после болезни')]
    name = models.CharField(max_length=25, choices=FEATURES_CHOICES)
    health = models.ForeignKey(Health, on_delete=models.CASCADE,
                             verbose_name='Особенности', 
                             related_name='features')

    class Meta:
        verbose_name = 'Особенности'
        verbose_name_plural = 'Особенности'

    def __str__(self):
        return self.name 

class Pet(models.Model):
    GENDER_CHOICES = [('M', 'Male'),('F', 'Female'),('O', 'Other')]
    WOOL_CHOICES = [('К','Короткая'), ('С','Средняя'), ('Д','Длинная')]
    ORIGIN_CHOICES = [('Ул','Подобран на улице'), ('За','Куплен у заводчика'),
                    ('Пр','Взят из приюта'), ('Вы','Куплен на выставке'), 
                    ('Ма','Куплен в магазине'), ('Бо','Спизжен у бомжей')]
    name = models.CharField(max_length=100)
    kind = models.ForeignKey(Kind, on_delete=models.CASCADE, 
                        verbose_name='Питомец', related_name='pet')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, 
                        verbose_name='Питомец', related_name='pet')
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    weight = models.FloatField()
    wool_type = models.CharField(max_length=8, choices=WOOL_CHOICES)
    chip_number = models.CharField(max_length=18) 
    origin = models.CharField(max_length=18, choices=ORIGIN_CHOICES)
    health = models.OneToOneField(Health, on_delete=models.CASCADE, 
                        verbose_name='Здоровье', related_name='pet')
    procedures = models.OneToOneField(Procedures, related_name='pet',
                on_delete=models.CASCADE, verbose_name='Процедуры')
    master = models.ForeignKey(User, on_delete=models.CASCADE, 
                        verbose_name='Питомец', related_name='pet') 

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'

    def __str__(self):
        return self.name 
    
class PetPhotos(models.Model):
    image = models.ImageField(upload_to='pet/images/')
    is_main = models.BooleanField(blank=False, null=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE,
            verbose_name='Фото питомца', related_name='petphotos')

    class Meta:
        verbose_name = 'Фото питомца'
        verbose_name_plural = 'Фото питомца'