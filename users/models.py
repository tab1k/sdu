from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    father = models.CharField(max_length=155)
    student_number = models.PositiveBigIntegerField(blank=True, null=True)
    photo = models.ImageField(blank=False, null=False)
    birth_date = models.CharField(max_length=155)
    program = models.CharField(max_length=155)
    advisor = models.CharField(max_length=155)
    status = models.BooleanField(default=True)
    balance = models.PositiveBigIntegerField(blank=True, null=True)
    ent_score = models.PositiveIntegerField(blank=True, null=True)
    grant_type = models.CharField(max_length=255)
    email = models.EmailField(blank=False)
    registered_on = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('male', 'Мужской'), ('female', 'Женский'), ('other', 'Другой')],
                              blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'