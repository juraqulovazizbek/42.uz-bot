from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    chat_id = models.CharField(max_length=255, unique=True)
    telegram_username = models.CharField(max_length=255, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'

    def __str__(self):
        return self.username