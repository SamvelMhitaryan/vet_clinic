# Generated by Django 5.0 on 2023-12-21 10:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to=settings.AUTH_USER_MODEL, verbose_name='Питомец'),
        ),
        migrations.AddField(
            model_name='petphotos',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petphotos', to='pet.pet', verbose_name='Фото питомца'),
        ),
        migrations.AddField(
            model_name='pet',
            name='procedures',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pet', to='pet.procedures', verbose_name='Процедуры'),
        ),
    ]