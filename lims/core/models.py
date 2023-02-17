from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


def user_profile_photo_path(instance, filename):
    user_id = instance.id
    return f'user_photos/user-{user_id}/{filename}'


class CustomUser(AbstractUser):
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=user_profile_photo_path, default='default.png')
    telephone = models.CharField(max_length=18, blank=True)
    email = models.EmailField(blank=False)
    secret_question = models.CharField(blank=False, max_length=150, default='Имя первого питомца')
    secret_answer = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return reverse('core:profile', kwargs={'user_id': self.pk})